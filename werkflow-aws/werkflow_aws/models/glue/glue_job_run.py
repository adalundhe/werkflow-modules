from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .glue_notification_property import GlueNotificationProperty
from .glue_predecessor import GluePredecessor


class GlueJobRun(BaseModel):
    Id: StrictStr | None = None
    Attempt: StrictInt | None = None
    PreviousRunId: StrictStr | None = None
    TriggerName: StrictStr | None = None
    JobName: StrictStr | None = None
    JobMode: StrictStr | None = None
    JobRunQueuingEnabled: StrictBool | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    JobRunState: StrictStr | None = None
    Arguments: dict[StrictStr, StrictStr] | None = None
    ErrorMessage: StrictStr | None = None
    PredecessorRuns: list[GluePredecessor] | None = None
    AllocatedCapacity: StrictInt | None = None
    ExecutionTime: StrictInt | None = None
    Timeout: StrictInt | None = None
    MaxCapacity: StrictFloat | StrictInt | None = None
    WorkerType: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    SecurityConfiguration: StrictStr | None = None
    LogGroupName: StrictStr | None = None
    NotificationProperty: GlueNotificationProperty | None = None
    GlueVersion: StrictStr | None = None
    DPUSeconds: StrictFloat | StrictInt | None = None
    ExecutionClass: StrictStr | None = None
    MaintenanceWindow: StrictStr | None = None
    ProfileName: StrictStr | None = None
    StateDetail: StrictStr | None = None
    ExecutionRoleSessionPolicy: StrictStr | None = None
