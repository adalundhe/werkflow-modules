from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_jdbc_connector_options import GlueJDBCConnectorOptions
from .glue_schema import GlueSchema


class GlueJDBCConnectorSource(BaseModel):
    Name: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    ConnectorName: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    AdditionalOptions: GlueJDBCConnectorOptions | None = None
    ConnectionTable: StrictStr | None = None
    Query: StrictStr | None = None
    OutputSchemas: list[GlueSchema] | None = None
