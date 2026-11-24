from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_container_instance_details import GuardDutyContainerInstanceDetails
from .guard_duty_fargate_details import GuardDutyFargateDetails


class GuardDutyCoverageEcsClusterDetails(BaseModel):
    ClusterName: StrictStr | None = None
    FargateDetails: GuardDutyFargateDetails | None = None
    ContainerInstanceDetails: GuardDutyContainerInstanceDetails | None = None
