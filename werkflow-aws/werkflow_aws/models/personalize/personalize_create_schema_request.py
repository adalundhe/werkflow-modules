from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class PersonalizeCreateSchemaRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: StrictStr
    schema_: StrictStr = Field(alias='schema')
    domain: Literal['ECOMMERCE', 'VIDEO_ON_DEMAND'] | None = None
