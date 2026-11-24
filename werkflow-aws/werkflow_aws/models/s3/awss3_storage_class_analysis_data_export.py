from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_analytics_export_destination import AWSS3AnalyticsExportDestination


class AWSS3StorageClassAnalysisDataExport(BaseModel):
    OutputSchemaVersion: StrictStr | None = None
    Destination: AWSS3AnalyticsExportDestination | None = None
