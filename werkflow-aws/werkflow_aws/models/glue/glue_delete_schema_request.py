from __future__ import annotations
from pydantic import BaseModel
from .glue_schema_id import GlueSchemaId


class GlueDeleteSchemaRequest(BaseModel):
    SchemaId: GlueSchemaId
