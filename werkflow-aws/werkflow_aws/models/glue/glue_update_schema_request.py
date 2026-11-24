from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_schema_id import GlueSchemaId
from .glue_schema_version_number import GlueSchemaVersionNumber


class GlueUpdateSchemaRequest(BaseModel):
    SchemaId: GlueSchemaId
    SchemaVersionNumber: GlueSchemaVersionNumber | None = None
    Compatibility: Literal['NONE', 'DISABLED', 'BACKWARD', 'BACKWARD_ALL', 'FORWARD', 'FORWARD_ALL', 'FULL', 'FULL_ALL'] | None = None
    Description: StrictStr | None = None
