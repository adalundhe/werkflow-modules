from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema import GlueSchema


class GlueCatalogIcebergSource(BaseModel):
    Name: StrictStr | None = None
    Database: StrictStr | None = None
    Table: StrictStr | None = None
    AdditionalIcebergOptions: dict[StrictStr, StrictStr] | None = None
    OutputSchemas: list[GlueSchema] | None = None
