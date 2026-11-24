from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class IoTDescribeIndexResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    indexName: StrictStr | None = None
    indexStatus: StrictStr | None = None
    schema_: StrictStr | None = Field(default=None, alias='schema')
    ResponseMetadata: dict[str, Any] | None = None
