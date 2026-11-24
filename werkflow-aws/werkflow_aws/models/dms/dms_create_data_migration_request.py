from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .dms_source_data_setting import DMSSourceDataSetting
from .dms_tag import DMSTag
from .dms_target_data_setting import DMSTargetDataSetting


class DMSCreateDataMigrationRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    DataMigrationType: Literal['full-load', 'cdc', 'full-load-and-cdc']
    ServiceAccessRoleArn: StrictStr
    DataMigrationName: StrictStr | None = None
    EnableCloudwatchLogs: StrictBool | None = None
    SourceDataSettings: list[DMSSourceDataSetting] | None = None
    TargetDataSettings: list[DMSTargetDataSetting] | None = None
    NumberOfJobs: StrictInt | None = None
    Tags: list[DMSTag] | None = None
    SelectionRules: StrictStr | None = None
