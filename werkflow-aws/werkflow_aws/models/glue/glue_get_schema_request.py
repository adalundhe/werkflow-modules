from __future__ import annotations
from pydantic import BaseModel
from .glue_schema_id import GlueSchemaId


class GlueGetSchemaRequest(BaseModel):
    SchemaId: GlueSchemaId
