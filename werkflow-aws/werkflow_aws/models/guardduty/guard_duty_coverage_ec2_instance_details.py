from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_agent_details import GuardDutyAgentDetails


class GuardDutyCoverageEc2InstanceDetails(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    AgentDetails: GuardDutyAgentDetails | None = None
    ManagementType: StrictStr | None = None
