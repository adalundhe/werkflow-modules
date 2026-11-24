from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_auto_data_quality import GlueAutoDataQuality
from .glue_direct_schema_change_policy import GlueDirectSchemaChangePolicy
from .glue_schema import GlueSchema


class GlueS3HyperDirectTarget(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    Format: StrictStr | None = None
    PartitionKeys: list[list[StrictStr]] | None = None
    Path: StrictStr | None = None
    Compression: StrictStr | None = None
    SchemaChangePolicy: GlueDirectSchemaChangePolicy | None = None
    AutoDataQuality: GlueAutoDataQuality | None = None
    OutputSchemas: list[GlueSchema] | None = None
