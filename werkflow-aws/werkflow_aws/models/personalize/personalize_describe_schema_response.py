from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field
from .personalize_dataset_schema import PersonalizeDatasetSchema


class PersonalizeDescribeSchemaResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    schema_: PersonalizeDatasetSchema | None = Field(default=None, alias='schema')
    ResponseMetadata: dict[str, Any] | None = None
