from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateSnapshotScheduleRequest(BaseModel):
    ScheduleDefinitions: list[StrictStr] | None = None
    ScheduleIdentifier: StrictStr | None = None
    ScheduleDescription: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
    DryRun: StrictBool | None = None
    NextInvocations: StrictInt | None = None
