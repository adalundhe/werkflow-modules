from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_checkpoint_configuration import KinesisAnalyticsCheckpointConfiguration
from .kinesis_analytics_monitoring_configuration import KinesisAnalyticsMonitoringConfiguration
from .kinesis_analytics_parallelism_configuration import KinesisAnalyticsParallelismConfiguration


class KinesisAnalyticsFlinkApplicationConfiguration(BaseModel):
    CheckpointConfiguration: KinesisAnalyticsCheckpointConfiguration | None = None
    MonitoringConfiguration: KinesisAnalyticsMonitoringConfiguration | None = None
    ParallelismConfiguration: KinesisAnalyticsParallelismConfiguration | None = None
