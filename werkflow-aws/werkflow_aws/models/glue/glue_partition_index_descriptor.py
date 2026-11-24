from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_backfill_error import GlueBackfillError
from .glue_key_schema_element import GlueKeySchemaElement


class GluePartitionIndexDescriptor(BaseModel):
    IndexName: StrictStr | None = None
    Keys: list[GlueKeySchemaElement] | None = None
    IndexStatus: StrictStr | None = None
    BackfillErrors: list[GlueBackfillError] | None = None
