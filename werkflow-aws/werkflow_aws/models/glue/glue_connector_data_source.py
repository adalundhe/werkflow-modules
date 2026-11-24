from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema


class GlueConnectorDataSource(BaseModel):
    Name: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    Data: dict[StrictStr, StrictStr] | None = None
    OutputSchemas: list[GlueSchema] | None = None
