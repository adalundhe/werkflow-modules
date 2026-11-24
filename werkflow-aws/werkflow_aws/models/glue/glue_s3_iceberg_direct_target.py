from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_auto_data_quality import GlueAutoDataQuality
from .glue_direct_schema_change_policy import GlueDirectSchemaChangePolicy
from .glue_schema import GlueSchema


class GlueS3IcebergDirectTarget(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    PartitionKeys: list[list[StrictStr]] | None = None
    Path: StrictStr | None = None
    Format: StrictStr | None = None
    AdditionalOptions: dict[StrictStr, StrictStr] | None = None
    SchemaChangePolicy: GlueDirectSchemaChangePolicy | None = None
    AutoDataQuality: GlueAutoDataQuality | None = None
    Compression: StrictStr | None = None
    NumberTargetPartitions: StrictStr | None = None
    OutputSchemas: list[GlueSchema] | None = None
