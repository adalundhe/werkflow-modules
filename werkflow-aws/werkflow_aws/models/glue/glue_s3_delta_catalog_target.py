from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_auto_data_quality import GlueAutoDataQuality
from .glue_catalog_schema_change_policy import GlueCatalogSchemaChangePolicy
from .glue_schema import GlueSchema


class GlueS3DeltaCatalogTarget(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    PartitionKeys: list[list[StrictStr]] | None = None
    Table: StrictStr | None = None
    Database: StrictStr | None = None
    AdditionalOptions: dict[StrictStr, StrictStr] | None = None
    SchemaChangePolicy: GlueCatalogSchemaChangePolicy | None = None
    AutoDataQuality: GlueAutoDataQuality | None = None
    OutputSchemas: list[GlueSchema] | None = None
