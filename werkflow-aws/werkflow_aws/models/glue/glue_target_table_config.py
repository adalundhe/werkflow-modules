from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_integration_partition import GlueIntegrationPartition


class GlueTargetTableConfig(BaseModel):
    UnnestSpec: StrictStr | None = None
    PartitionSpec: list[GlueIntegrationPartition] | None = None
    TargetTableName: StrictStr | None = None
    IntegrationArn: StrictStr | None = None
