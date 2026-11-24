from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_schema_id import GlueSchemaId


class GlueGetSchemaByDefinitionRequest(BaseModel):
    SchemaId: GlueSchemaId
    SchemaDefinition: StrictStr
