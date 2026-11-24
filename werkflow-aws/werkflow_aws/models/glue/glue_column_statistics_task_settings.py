from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_execution_attempt import GlueExecutionAttempt
from .glue_schedule import GlueSchedule


class GlueColumnStatisticsTaskSettings(BaseModel):
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    Schedule: GlueSchedule | None = None
    ColumnNameList: list[StrictStr] | None = None
    CatalogID: StrictStr | None = None
    Role: StrictStr | None = None
    SampleSize: StrictFloat | StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    ScheduleType: StrictStr | None = None
    SettingSource: StrictStr | None = None
    LastExecutionAttempt: GlueExecutionAttempt | None = None
