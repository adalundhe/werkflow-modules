from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_iceberg_document import GlueIcebergDocument


class GlueIcebergStructField(BaseModel):
    Id: StrictInt | None = None
    Name: StrictStr | None = None
    Type: GlueIcebergDocument | None = None
    Required: StrictBool | None = None
    Doc: StrictStr | None = None
    InitialDefault: GlueIcebergDocument | None = None
    WriteDefault: GlueIcebergDocument | None = None
