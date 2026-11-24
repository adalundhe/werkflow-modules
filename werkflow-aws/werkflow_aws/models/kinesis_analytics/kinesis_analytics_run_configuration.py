from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_application_restore_configuration import KinesisAnalyticsApplicationRestoreConfiguration
from .kinesis_analytics_flink_run_configuration import KinesisAnalyticsFlinkRunConfiguration
from .kinesis_analytics_sql_run_configuration import KinesisAnalyticsSqlRunConfiguration


class KinesisAnalyticsRunConfiguration(BaseModel):
    FlinkRunConfiguration: KinesisAnalyticsFlinkRunConfiguration | None = None
    SqlRunConfigurations: list[KinesisAnalyticsSqlRunConfiguration] | None = None
    ApplicationRestoreConfiguration: KinesisAnalyticsApplicationRestoreConfiguration | None = None
