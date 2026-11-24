from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_source_table_config import GlueSourceTableConfig
from .glue_target_table_config import GlueTargetTableConfig


class GlueGetIntegrationTablePropertiesResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    TableName: StrictStr | None = None
    SourceTableConfig: GlueSourceTableConfig | None = None
    TargetTableConfig: GlueTargetTableConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
