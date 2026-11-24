from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_coverage_ec2_instance_details import GuardDutyCoverageEc2InstanceDetails
from .guard_duty_coverage_ecs_cluster_details import GuardDutyCoverageEcsClusterDetails
from .guard_duty_coverage_eks_cluster_details import GuardDutyCoverageEksClusterDetails


class GuardDutyCoverageResourceDetails(BaseModel):
    EksClusterDetails: GuardDutyCoverageEksClusterDetails | None = None
    EcsClusterDetails: GuardDutyCoverageEcsClusterDetails | None = None
    Ec2InstanceDetails: GuardDutyCoverageEc2InstanceDetails | None = None
    ResourceType: StrictStr | None = None
