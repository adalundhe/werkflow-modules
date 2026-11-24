from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_application_configuration_description import KinesisAnalyticsApplicationConfigurationDescription
from .kinesis_analytics_application_maintenance_configuration_description import KinesisAnalyticsApplicationMaintenanceConfigurationDescription
from .kinesis_analytics_cloud_watch_logging_option_description import KinesisAnalyticsCloudWatchLoggingOptionDescription


class KinesisAnalyticsApplicationDetail(BaseModel):
    ApplicationARN: StrictStr | None = None
    ApplicationDescription: StrictStr | None = None
    ApplicationName: StrictStr | None = None
    RuntimeEnvironment: StrictStr | None = None
    ServiceExecutionRole: StrictStr | None = None
    ApplicationStatus: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    CreateTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdateTimestamp: datetime.datetime | StrictStr | None = None
    ApplicationConfigurationDescription: KinesisAnalyticsApplicationConfigurationDescription | None = None
    CloudWatchLoggingOptionDescriptions: list[KinesisAnalyticsCloudWatchLoggingOptionDescription] | None = None
    ApplicationMaintenanceConfigurationDescription: KinesisAnalyticsApplicationMaintenanceConfigurationDescription | None = None
    ApplicationVersionUpdatedFrom: StrictInt | None = None
    ApplicationVersionRolledBackFrom: StrictInt | None = None
    ApplicationVersionCreateTimestamp: datetime.datetime | StrictStr | None = None
    ConditionalToken: StrictStr | None = None
    ApplicationVersionRolledBackTo: StrictInt | None = None
    ApplicationMode: StrictStr | None = None
