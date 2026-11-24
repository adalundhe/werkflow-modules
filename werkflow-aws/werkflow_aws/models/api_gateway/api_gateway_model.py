from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class APIGatewayModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    schema_: StrictStr | None = Field(default=None, alias='schema')
    contentType: StrictStr | None = None
