from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema_id import GlueSchemaId
from .glue_schema_version_number import GlueSchemaVersionNumber


class GlueGetSchemaVersionRequest(BaseModel):
    SchemaId: GlueSchemaId | None = None
    SchemaVersionId: StrictStr | None = None
    SchemaVersionNumber: GlueSchemaVersionNumber | None = None
