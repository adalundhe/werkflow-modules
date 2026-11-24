from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dms_data_migration_settings import DMSDataMigrationSettings
from .dms_data_migration_statistics import DMSDataMigrationStatistics
from .dms_source_data_setting import DMSSourceDataSetting
from .dms_target_data_setting import DMSTargetDataSetting


class DMSDataMigration(BaseModel):
    DataMigrationName: StrictStr | None = None
    DataMigrationArn: StrictStr | None = None
    DataMigrationCreateTime: datetime.datetime | StrictStr | None = None
    DataMigrationStartTime: datetime.datetime | StrictStr | None = None
    DataMigrationEndTime: datetime.datetime | StrictStr | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    MigrationProjectArn: StrictStr | None = None
    DataMigrationType: StrictStr | None = None
    DataMigrationSettings: DMSDataMigrationSettings | None = None
    SourceDataSettings: list[DMSSourceDataSetting] | None = None
    TargetDataSettings: list[DMSTargetDataSetting] | None = None
    DataMigrationStatistics: DMSDataMigrationStatistics | None = None
    DataMigrationStatus: StrictStr | None = None
    PublicIpAddresses: list[StrictStr] | None = None
    DataMigrationCidrBlocks: list[StrictStr] | None = None
    LastFailureMessage: StrictStr | None = None
    StopReason: StrictStr | None = None
