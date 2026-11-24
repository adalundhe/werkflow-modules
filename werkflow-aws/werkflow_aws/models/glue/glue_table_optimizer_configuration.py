from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_compaction_configuration import GlueCompactionConfiguration
from .glue_orphan_file_deletion_configuration import GlueOrphanFileDeletionConfiguration
from .glue_retention_configuration import GlueRetentionConfiguration
from .glue_table_optimizer_vpc_configuration import GlueTableOptimizerVpcConfiguration


class GlueTableOptimizerConfiguration(BaseModel):
    roleArn: StrictStr | None = None
    enabled: StrictBool | None = None
    vpcConfiguration: GlueTableOptimizerVpcConfiguration | None = None
    compactionConfiguration: GlueCompactionConfiguration | None = None
    retentionConfiguration: GlueRetentionConfiguration | None = None
    orphanFileDeletionConfiguration: GlueOrphanFileDeletionConfiguration | None = None
