from pydantic import ConfigDict
from pydantic import BaseModel, Field, constr
from datetime import datetime

class ObjectDataModel(BaseModel):
    # Use model_config to allow extra fields
    model_config = ConfigDict(extra='allow')

    year: int
    price: float
    cpu_model: str = Field(alias="CPU model")
    hard_disk_size: str = Field(alias="Hard disk size")
    color: str


class updateObjectPayloadModel(BaseModel):
    name: str
    data: ObjectDataModel


class UpdateObjectDataModel(BaseModel):
    model_config = ConfigDict(extra='allow', populate_by_name=True)

    year: int
    price: float
    cpu_model: str = Field(..., alias="cpu_model")  # Ensure alias matches input data
    hard_disk_size: str = Field(..., alias="hard_disk_size")  # Ensure alias matches input data
    color: str

class updateObjectResponseModel(BaseModel):
    id: str  # Ensure type matches input data (or change to int if needed)
    name: str = Field(..., max_length=100, description="Name of the object.")
    data: UpdateObjectDataModel
    updatedAt: str = Field(..., alias="updatedAt", description="Timestamp when the object was last updated.")

    model_config = ConfigDict(populate_by_name=True)
