from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_configuration import EMRConfiguration
from .emr_session_monitoring_configuration import EMRSessionMonitoringConfiguration
from .emr_tag import EMRTag


class EMRStartSessionRequest(BaseModel):
    ClusterId: StrictStr
    Name: StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
    EngineConfigurations: list[EMRConfiguration] | None = None
    MonitoringConfiguration: EMRSessionMonitoringConfiguration | None = None
    SessionIdleTimeoutInMinutes: StrictInt | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[EMRTag] | None = None
