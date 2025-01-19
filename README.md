
# API Testing Framework with Pydantic

Welcome to the **API Testing Framework with Pydantic**, a Python-based framework designed to validate API responses with precision and reliability. This framework leverages **Pydantic** for data validation and parsing, ensuring your API interactions meet the expected data schema.


## Framework Structure

Here’s an overview of the project structure:
```
Api_testing_framework/
│ 
├── models/
│   ├── __init__.py
│   ├── user_models.py
│   ├── post_models.py
│ 
├── API_Utilities/
│   ├── __init__.py
│   ├── api_actions.py
│ 
├── testcases/
│   ├── __init__.py
│   ├── test_01_getUser.py
│   ├── test_02_createUser.py
│   ├── test_03_getPosts.py
│   ├── test_04_createPosts.py
│   ├── conftest.py
│ 
├── .env.staging
├── .env.production
│ 
├── requirements.txt
└── README.md
```


## Features

- **Pydantic for Validation**: Ensures API responses conform to predefined schemas.
- **Reusable Models**: Models can be shared across different test cases for consistency.
- **Environment-Specific Configurations**: `.env.staging` and `.env.production` for environment-based configurations.
- **Modular Design**: Clear separation of concerns between models, utilities, and test cases.


## Installation

Clone the repository:
   ```bash
   git clone https://github.com/DipankarDandapat/API_Automation_With_Pydantic.git
   cd API_Automation_With_Pydantic
  ```


