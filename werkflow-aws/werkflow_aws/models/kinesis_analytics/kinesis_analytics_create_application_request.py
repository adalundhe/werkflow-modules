from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_configuration import KinesisAnalyticsApplicationConfiguration
from .kinesis_analytics_cloud_watch_logging_option import KinesisAnalyticsCloudWatchLoggingOption
from .kinesis_analytics_tag import KinesisAnalyticsTag


class KinesisAnalyticsCreateApplicationRequest(BaseModel):
    ApplicationName: StrictStr
    RuntimeEnvironment: Literal['SQL-1_0', 'FLINK-1_6', 'FLINK-1_8', 'ZEPPELIN-FLINK-1_0', 'FLINK-1_11', 'FLINK-1_13', 'ZEPPELIN-FLINK-2_0', 'FLINK-1_15', 'ZEPPELIN-FLINK-3_0', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-2_2', 'FLINK-2_3']
    ServiceExecutionRole: StrictStr
    ApplicationDescription: StrictStr | None = None
    ApplicationConfiguration: KinesisAnalyticsApplicationConfiguration | None = None
    CloudWatchLoggingOptions: list[KinesisAnalyticsCloudWatchLoggingOption] | None = None
    Tags: list[KinesisAnalyticsTag] | None = None
    ApplicationMode: Literal['STREAMING', 'INTERACTIVE'] | None = None
