from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema


class GlueSparkConnectorTarget(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    ConnectionName: StrictStr | None = None
    ConnectorName: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    AdditionalOptions: dict[StrictStr, StrictStr] | None = None
    OutputSchemas: list[GlueSchema] | None = None
