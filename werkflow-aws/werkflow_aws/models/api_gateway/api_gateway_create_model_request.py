from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class APIGatewayCreateModelRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    restApiId: StrictStr
    name: StrictStr
    contentType: StrictStr
    description: StrictStr | None = None
    schema_: StrictStr | None = Field(default=None, alias='schema')
