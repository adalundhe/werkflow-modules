from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_reference_data_source import KinesisAnalyticsReferenceDataSource


class KinesisAnalyticsAddApplicationReferenceDataSourceRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt
    ReferenceDataSource: KinesisAnalyticsReferenceDataSource
