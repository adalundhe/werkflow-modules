from __future__ import annotations
from pydantic import BaseModel
from .ses_message_insights_data_source import SESMessageInsightsDataSource
from .ses_metrics_data_source import SESMetricsDataSource


class SESExportDataSource(BaseModel):
    MetricsDataSource: SESMetricsDataSource | None = None
    MessageInsightsDataSource: SESMessageInsightsDataSource | None = None
