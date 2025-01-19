import os

import requests
from dotenv import load_dotenv
import pytest
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from API_Utilities.api_actions import APIClient

# Initialize the TEST_RESULTS dictionary
TEST_RESULTS = {}

@pytest.fixture(scope="session")
def session():
    """
    Create a session with retry logic.
    """
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


@pytest.fixture(scope="session")
def api_client(session):
    return APIClient(session)

def load_environment_file(env):
    """
    Load the specified environment file.
    """
    env_file = f".env.{env}"
    if os.path.exists(env_file):
        load_dotenv(env_file, override=True)
    else:
        raise FileNotFoundError(f"{env_file} does not exist.")

def pytest_addoption(parser):
    """
    Adds a custom command-line option to specify the environments.
    """
    parser.addoption(
        "--envs",
        action="store",
        default="staging,production",
        help="Specify environments as a comma-separated list: staging,production"
    )

def pytest_configure(config):
    """
    Configure the TEST_RESULTS dictionary based on the environments passed in `--envs`.
    """
    global TEST_RESULTS
    envs = config.getoption("envs").split(",")
    TEST_RESULTS = {env: {} for env in envs}

def pytest_collection_modifyitems(config, items):
    """
    Reorder test items to run tests for the specified environments first.
    """
    envs = config.getoption("envs").split(",")

    # Create a new ordered list of test items
    ordered_items = []

    # First, add tests for each environment in the specified order
    for env in envs:
        for item in items:
            # Check if the test is marked with the current environment
            if env in item.name or (hasattr(item, 'callspec') and
                                    hasattr(item.callspec, 'params') and
                                    env in item.callspec.params):
                ordered_items.append(item)

    # Replace the original items list with the ordered list
    items[:] = ordered_items

def pytest_generate_tests(metafunc):
    """
    Dynamically parameterize the `env` fixture based on the `--envs` option.
    """
    envs = metafunc.config.getoption("envs").split(",")
    if "env" in metafunc.fixturenames:
        metafunc.parametrize("env", envs, scope="function")

@pytest.fixture(scope="function")
def setup_env(env):
    """
    Automatically load the specified environment file for each test function.
    """
    load_environment_file(env)
    print(f"Loaded environment: {env}")
    return env

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     """
#     Hook to track test results after each test phase.
#     """
#     package_name = item.module.__name__.split(".")[1]
#     # Trim the test case path for easier readability
#     trimmed_package_path = item.nodeid.replace("testcases/", "").rsplit("::", 1)[0]
#
#     env = None
#     if hasattr(item, 'callspec'):
#         env = item.callspec.params.get('env')
#
#     if not env:
#         return
#
#     if package_name not in TEST_RESULTS[env]:
#         TEST_RESULTS[env][package_name] = {'passed': 0, 'failed': 0, 'skipped': 0, 'total': 0, 'details': [] }
#
#     if report.when == "setup":
#         # Increment total tests
#         TEST_RESULTS[env][package_name]['total'] += 1
#
#     elif report.when == "call":
#
#         test_details = {
#             "name": trimmed_package_path,
#             "outcome": report.outcome,
#             "duration": report.duration,
#             "skip_reason": None,
#             "fail_reason": None
#         }
#
#
#
#         if report.outcome == "passed":
#             TEST_RESULTS[env][package_name]['passed'] += 1
#         elif report.outcome == "failed":
#             TEST_RESULTS[env][package_name]['failed'] += 1
#             if hasattr(report.longrepr, 'reprcrash'):
#                 test_details["fail_reason"] = report.longrepr.reprcrash.message.splitlines()[0]
#             else:
#                 test_details["fail_reason"] = str(report.longrepr).splitlines()[0]
#         elif report.outcome == "skipped":
#             TEST_RESULTS[env][package_name]['skipped'] += 1
#             if isinstance(report.longrepr, tuple):
#                 test_details["skip_reason"] = str(report.longrepr[2])
#             else:
#                 test_details["skip_reason"] = str(report.longrepr)
#
#         # Add test details to the package
#         TEST_RESULTS[env][package_name]['details'].append(test_details)
#
# def pytest_terminal_summary(terminalreporter, exitstatus):
#
#     """
#     Print the test report at the end of the test run.
#     """
#     terminalreporter.write_line(generate_test_report())
#
#
# def generate_test_report():
#     """
#     Generate a formatted test report string.
#     """
#     report_lines = ["===== Test Execution Report ====="]
#
#     for env, packages in TEST_RESULTS.items():
#         report_lines.append(f"\nEnvironment: {env.upper()}")
#         report_lines.append("-" * 30)
#         failed_tests = []  # Collect failed tests for this environment
#
#         for package, results in packages.items():
#             report_lines.append(f"Project: {package}")
#             report_lines.append(f"  Total Tests:   {results['total']}")
#
#             if results['total'] > 0:
#                 # Calculate percentages
#                 pass_percentage = (results['passed'] / results['total']) * 100
#                 fail_percentage = (results['failed'] / results['total']) * 100
#                 skip_percentage = (results['skipped'] / results['total']) * 100
#
#                 report_lines.append(f"  Passed Tests:  {results['passed']} ({pass_percentage:.2f}%)")
#                 report_lines.append(f"  Failed Tests:  {results['failed']} ({fail_percentage:.2f}%)")
#                 report_lines.append(f"  Skipped Tests: {results['skipped']} ({skip_percentage:.2f}%)")
#             else:
#                 report_lines.append("  No tests executed in this package.")
#
#             # Collect failed test details
#             for result in results['details']:
#                 if result["outcome"] == "failed":
#                     failed_tests.append(
#                         f"    - {result['name']} - FAILED (Reason: {result['fail_reason']})"
#                     )
#
#         # Add failed test results for the environment
#         if failed_tests:
#             report_lines.append("\nFailed Test Results:")
#             report_lines.extend(failed_tests)
#
#     report_lines.append("\n===== End of Test Report =====")
#     return "\n".join(report_lines)
