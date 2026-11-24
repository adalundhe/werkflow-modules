from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_schema_id import GlueSchemaId


class GlueSchemaReference(BaseModel):
    SchemaId: GlueSchemaId | None = None
    SchemaVersionId: StrictStr | None = None
    SchemaVersionNumber: StrictInt | None = None
