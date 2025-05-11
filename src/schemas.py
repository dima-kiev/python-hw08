from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict, validator, root_validator


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=50)
    phone: str = Field(max_length=50)
    birthday: date | None
    description: Optional[str] = Field(None, max_length=150)


class ContactUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=50)
    phone: Optional[str] = Field(None, max_length=50)
    birthday: Optional[date] = None
    description: Optional[str] = Field(None, max_length=150)

    @root_validator(pre=True)
    def check_at_least_one_field(cls, values):
        if all(value is None for value in values.values()):
            raise ValueError("At least one field must be provided")
        return values


class ContactResponse(ContactModel):
    id: int
    model_config = ConfigDict(from_attributes=True)
