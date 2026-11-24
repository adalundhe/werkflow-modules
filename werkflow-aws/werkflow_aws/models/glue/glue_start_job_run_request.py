from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .glue_notification_property import GlueNotificationProperty


class GlueStartJobRunRequest(BaseModel):
    JobName: StrictStr
    JobRunQueuingEnabled: StrictBool | None = None
    JobRunId: StrictStr | None = None
    Arguments: dict[StrictStr, StrictStr] | None = None
    AllocatedCapacity: StrictInt | None = None
    Timeout: StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    NotificationProperty: GlueNotificationProperty | None = None
    WorkerType: Literal['Standard', 'G.1X', 'G.2X', 'G.4X', 'G.8X', 'G.025X', 'Z.2X', 'G.12X', 'G.16X', 'R.1X', 'R.2X', 'R.4X', 'R.8X'] | None = None
    NumberOfWorkers: StrictInt | None = None
    ExecutionClass: Literal['FLEX', 'STANDARD'] | None = None
    ExecutionRoleSessionPolicy: StrictStr | None = None
