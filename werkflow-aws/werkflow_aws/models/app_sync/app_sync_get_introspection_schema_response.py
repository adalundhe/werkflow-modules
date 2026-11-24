from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field, StrictBytes


class AppSyncGetIntrospectionSchemaResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, populate_by_name=True)

    schema_: StrictBytes | Any | None = Field(default=None, alias='schema')
    ResponseMetadata: dict[str, Any] | None = None
