from pydantic import BaseModel, ConfigDict

class Department(BaseModel):
    
    id: str
    name: str
    description: str


    model_config = ConfigDict(from_attributes=True)