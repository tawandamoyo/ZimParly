from pydantic import BaseModel, Field, computed_field
from typing import Optional

# This schema defines the base fields for an MP.
# It's the common denominator for creating and reading.
class MPBase(BaseModel):
    full_name: str
    honorific: Optional[str] = Field(None, description="e.g., The Hon., Mr. Speaker")
    party: Optional[str] = None
    constituency: Optional[str] = None
    biography: Optional[str] = None

# This is the schema used when creating a new MP via the API.
class MPCreate(MPBase):
    pass

# This schema defines the fields that can be updated on an existing MP.
# Notice how every field is Optional, allowing for partial updates.
class MPUpdate(BaseModel):
    full_name: Optional[str] = None
    honorific: Optional[str] = None
    party: Optional[str] = None
    constituency: Optional[str] = None
    biography: Optional[str] = None
    is_active: Optional[bool] = None

# This is the main schema for returning MP data from the API.
# It includes database-generated fields like `id` and `is_active`.
class MPRead(MPBase):
    id: int
    is_active: bool
    
    # This is a Pydantic v2 feature that computes a field on the fly.
    # It elegantly provides the formatted name we want in our API responses.
    @computed_field
    @property
    def display_name(self) -> str:
        return f"{self.honorific} {self.full_name}" if self.honorific else self.full_name

    class Config:
        from_attributes = True