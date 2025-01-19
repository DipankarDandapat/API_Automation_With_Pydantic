from pydantic import BaseModel, Field, constr
from pydantic import ConfigDict
from datetime import datetime
from typing import Dict, Optional



class MacBookRequestData(BaseModel):
    year: int
    price: float
    cpu_model: str = Field(alias="CPU model")
    hard_disk_size: str = Field(alias="Hard disk size")

class MacBookRequest(BaseModel):
    name: str
    data: MacBookRequestData

# Pydantic Model for API Response
class MacBookResponseData(BaseModel):
    # Use model_config to allow extra fields
    model_config = ConfigDict(extra='allow')

    # Make these fields optional with default values
    year: Optional[int] = None
    price: Optional[float] = None
    cpu_model: Optional[str] = Field(default=None, validation_alias="CPU model")
    hard_disk_size: Optional[str] = Field(default=None, validation_alias="Hard disk size")


class MacBookResponse(BaseModel):
    # Use model_config to allow extra fields
    model_config = ConfigDict(extra='allow')

    id: str
    name: str
    created_at: datetime = Field(validation_alias="createdAt")
    data: MacBookResponseData