from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .glue_schema_id import GlueSchemaId
from .glue_schema_version_number import GlueSchemaVersionNumber


class GlueGetSchemaVersionsDiffRequest(BaseModel):
    SchemaId: GlueSchemaId
    FirstSchemaVersionNumber: GlueSchemaVersionNumber
    SecondSchemaVersionNumber: GlueSchemaVersionNumber
    SchemaDiffType: Literal['SYNTAX_DIFF']
