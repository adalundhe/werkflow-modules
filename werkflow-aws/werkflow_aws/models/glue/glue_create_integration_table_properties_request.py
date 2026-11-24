from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_source_table_config import GlueSourceTableConfig
from .glue_target_table_config import GlueTargetTableConfig


class GlueCreateIntegrationTablePropertiesRequest(BaseModel):
    ResourceArn: StrictStr
    TableName: StrictStr
    SourceTableConfig: GlueSourceTableConfig | None = None
    TargetTableConfig: GlueTargetTableConfig | None = None
