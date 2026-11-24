from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema


class GlueDirectJDBCSource(BaseModel):
    Name: StrictStr | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    RedshiftTmpDir: StrictStr | None = None
    OutputSchemas: list[GlueSchema] | None = None
