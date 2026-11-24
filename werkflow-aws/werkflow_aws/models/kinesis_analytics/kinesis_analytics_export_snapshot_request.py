from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_export_destination_configuration import KinesisAnalyticsExportDestinationConfiguration


class KinesisAnalyticsExportSnapshotRequest(BaseModel):
    SnapshotName: StrictStr
    ExportDestinationConfiguration: KinesisAnalyticsExportDestinationConfiguration
