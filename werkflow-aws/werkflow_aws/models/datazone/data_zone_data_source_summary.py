from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_data_source_error_message import DataZoneDataSourceErrorMessage
from .data_zone_schedule_configuration import DataZoneScheduleConfiguration


class DataZoneDataSourceSummary(BaseModel):
    domainId: StrictStr | None = None
    environmentId: StrictStr | None = None
    connectionId: StrictStr | None = None
    dataSourceId: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    enableSetting: StrictStr | None = None
    schedule: DataZoneScheduleConfiguration | None = None
    lastRunStatus: StrictStr | None = None
    lastRunAt: datetime.datetime | StrictStr | None = None
    lastRunErrorMessage: DataZoneDataSourceErrorMessage | None = None
    lastRunAssetCount: StrictInt | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
