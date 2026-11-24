from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSDataMigrationSettings(BaseModel):
    NumberOfJobs: StrictInt | None = None
    CloudwatchLogsEnabled: StrictBool | None = None
    SelectionRules: StrictStr | None = None
