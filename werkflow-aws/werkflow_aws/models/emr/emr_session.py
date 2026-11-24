from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_configuration import EMRConfiguration
from .emr_session_monitoring_configuration import EMRSessionMonitoringConfiguration
from .emr_tag import EMRTag


class EMRSession(BaseModel):
    Id: StrictStr | None = None
    ClusterId: StrictStr | None = None
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    State: StrictStr | None = None
    StateChangeReason: StrictStr | None = None
    ReleaseLabel: StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
    AccountId: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    IdleSince: datetime.datetime | StrictStr | None = None
    EngineConfigurations: list[EMRConfiguration] | None = None
    MonitoringConfiguration: EMRSessionMonitoringConfiguration | None = None
    SessionIdleTimeoutInMinutes: StrictInt | None = None
    ServerUrl: StrictStr | None = None
    Tags: list[EMRTag] | None = None
