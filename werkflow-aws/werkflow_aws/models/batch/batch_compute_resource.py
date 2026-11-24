from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_compute_scaling_policy import BatchComputeScalingPolicy
from .batch_ec2_configuration import BatchEc2Configuration
from .batch_launch_template_specification import BatchLaunchTemplateSpecification
from .batch_managed_instances_provider import BatchManagedInstancesProvider


class BatchComputeResource(BaseModel):
    type: StrictStr | None = None
    allocationStrategy: StrictStr | None = None
    minvCpus: StrictInt | None = None
    maxvCpus: StrictInt | None = None
    desiredvCpus: StrictInt | None = None
    instanceTypes: list[StrictStr] | None = None
    imageId: StrictStr | None = None
    subnets: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
    ec2KeyPair: StrictStr | None = None
    instanceRole: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    placementGroup: StrictStr | None = None
    bidPercentage: StrictInt | None = None
    spotIamFleetRole: StrictStr | None = None
    launchTemplate: BatchLaunchTemplateSpecification | None = None
    ec2Configuration: list[BatchEc2Configuration] | None = None
    scalingPolicy: BatchComputeScalingPolicy | None = None
    managedInstancesProvider: BatchManagedInstancesProvider | None = None
    capacityTags: dict[StrictStr, StrictStr] | None = None
