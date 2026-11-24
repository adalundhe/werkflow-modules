from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_compaction_metrics import GlueCompactionMetrics
from .glue_orphan_file_deletion_metrics import GlueOrphanFileDeletionMetrics
from .glue_retention_metrics import GlueRetentionMetrics
from .glue_run_metrics import GlueRunMetrics


class GlueTableOptimizerRun(BaseModel):
    eventType: StrictStr | None = None
    startTimestamp: datetime.datetime | StrictStr | None = None
    endTimestamp: datetime.datetime | StrictStr | None = None
    metrics: GlueRunMetrics | None = None
    error: StrictStr | None = None
    compactionMetrics: GlueCompactionMetrics | None = None
    compactionStrategy: StrictStr | None = None
    retentionMetrics: GlueRetentionMetrics | None = None
    orphanFileDeletionMetrics: GlueOrphanFileDeletionMetrics | None = None
