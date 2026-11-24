from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_schema_id import GlueSchemaId


class GlueListSchemaVersionsRequest(BaseModel):
    SchemaId: GlueSchemaId
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
