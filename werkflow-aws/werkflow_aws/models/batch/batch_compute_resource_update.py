from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .batch_compute_scaling_policy import BatchComputeScalingPolicy
from .batch_ec2_configuration import BatchEc2Configuration
from .batch_launch_template_specification import BatchLaunchTemplateSpecification
from .batch_update_managed_instances_provider_configuration import BatchUpdateManagedInstancesProviderConfiguration


class BatchComputeResourceUpdate(BaseModel):
    minvCpus: StrictInt | None = None
    maxvCpus: StrictInt | None = None
    desiredvCpus: StrictInt | None = None
    subnets: list[StrictStr] | None = None
    securityGroupIds: list[StrictStr] | None = None
    allocationStrategy: Literal['BEST_FIT_PROGRESSIVE', 'BEST_FIT_PROGRESSIVE_ORDERED', 'SPOT_CAPACITY_OPTIMIZED', 'SPOT_PRICE_CAPACITY_OPTIMIZED', 'SPOT_CAPACITY_OPTIMIZED_PRIORITIZED'] | None = None
    instanceTypes: list[StrictStr] | None = None
    ec2KeyPair: StrictStr | None = None
    instanceRole: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    placementGroup: StrictStr | None = None
    bidPercentage: StrictInt | None = None
    launchTemplate: BatchLaunchTemplateSpecification | None = None
    ec2Configuration: list[BatchEc2Configuration] | None = None
    updateToLatestImageVersion: StrictBool | None = None
    type: Literal['EC2', 'SPOT', 'FARGATE', 'FARGATE_SPOT', 'ECS_MANAGED_INSTANCES'] | None = None
    imageId: StrictStr | None = None
    scalingPolicy: BatchComputeScalingPolicy | None = None
    managedInstancesProvider: BatchUpdateManagedInstancesProviderConfiguration | None = None
    capacityTags: dict[StrictStr, StrictStr] | None = None
