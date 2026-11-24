from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_application_configuration_update import KinesisAnalyticsApplicationConfigurationUpdate
from .kinesis_analytics_cloud_watch_logging_option_update import KinesisAnalyticsCloudWatchLoggingOptionUpdate
from .kinesis_analytics_run_configuration_update import KinesisAnalyticsRunConfigurationUpdate


class KinesisAnalyticsUpdateApplicationRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt | None = None
    ApplicationConfigurationUpdate: KinesisAnalyticsApplicationConfigurationUpdate | None = None
    ServiceExecutionRoleUpdate: StrictStr | None = None
    RunConfigurationUpdate: KinesisAnalyticsRunConfigurationUpdate | None = None
    CloudWatchLoggingOptionUpdates: list[KinesisAnalyticsCloudWatchLoggingOptionUpdate] | None = None
    ConditionalToken: StrictStr | None = None
    RuntimeEnvironmentUpdate: Literal['SQL-1_0', 'FLINK-1_6', 'FLINK-1_8', 'ZEPPELIN-FLINK-1_0', 'FLINK-1_11', 'FLINK-1_13', 'ZEPPELIN-FLINK-2_0', 'FLINK-1_15', 'ZEPPELIN-FLINK-3_0', 'FLINK-1_18', 'FLINK-1_19', 'FLINK-1_20', 'FLINK-2_2', 'FLINK-2_3'] | None = None
