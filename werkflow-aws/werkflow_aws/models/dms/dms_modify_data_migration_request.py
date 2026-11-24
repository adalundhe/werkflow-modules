from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dms_source_data_setting import DMSSourceDataSetting
from .dms_target_data_setting import DMSTargetDataSetting


class DMSModifyDataMigrationRequest(BaseModel):
    DataMigrationIdentifier: StrictStr
    DataMigrationName: StrictStr | None = None
    EnableCloudwatchLogs: StrictBool | None = None
    ServiceAccessRoleArn: StrictStr | None = None
    DataMigrationType: Literal['full-load', 'cdc', 'full-load-and-cdc'] | None = None
    SourceDataSettings: list[DMSSourceDataSetting] | None = None
    TargetDataSettings: list[DMSTargetDataSetting] | None = None
    NumberOfJobs: StrictInt | None = None
    SelectionRules: StrictStr | None = None
