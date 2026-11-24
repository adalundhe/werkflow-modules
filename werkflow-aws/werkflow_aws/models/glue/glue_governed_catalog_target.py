from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_catalog_schema_change_policy import GlueCatalogSchemaChangePolicy


class GlueGovernedCatalogTarget(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    PartitionKeys: list[list[StrictStr]] | None = None
    Table: StrictStr | None = None
    Database: StrictStr | None = None
    SchemaChangePolicy: GlueCatalogSchemaChangePolicy | None = None
