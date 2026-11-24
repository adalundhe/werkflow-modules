from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class BedrockRuntimeJsonSchemaDefinition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    schema_: StrictStr = Field(alias='schema')
    name: StrictStr | None = None
    description: StrictStr | None = None
