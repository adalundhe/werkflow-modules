from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema


class GlueAthenaConnectorSource(BaseModel):
    Name: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    ConnectorName: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    ConnectionTable: StrictStr | None = None
    SchemaName: StrictStr | None = None
    OutputSchemas: list[GlueSchema] | None = None
