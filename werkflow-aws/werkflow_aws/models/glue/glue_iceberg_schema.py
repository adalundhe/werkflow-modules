from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_iceberg_struct_field import GlueIcebergStructField


class GlueIcebergSchema(BaseModel):
    SchemaId: StrictInt | None = None
    IdentifierFieldIds: list[StrictInt] | None = None
    Type: StrictStr | None = None
    Fields: list[GlueIcebergStructField] | None = None
