from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .emr_auto_scaling_policy_description import EMRAutoScalingPolicyDescription
from .emr_configuration import EMRConfiguration
from .emr_ebs_block_device import EMREbsBlockDevice
from .emr_instance_group_status import EMRInstanceGroupStatus
from .emr_shrink_policy import EMRShrinkPolicy


class EMRInstanceGroup(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Market: StrictStr | None = None
    InstanceGroupType: StrictStr | None = None
    BidPrice: StrictStr | None = None
    InstanceType: StrictStr | None = None
    RequestedInstanceCount: StrictInt | None = None
    RunningInstanceCount: StrictInt | None = None
    Status: EMRInstanceGroupStatus | None = None
    Configurations: list[EMRConfiguration] | None = None
    ConfigurationsVersion: StrictInt | None = None
    LastSuccessfullyAppliedConfigurations: list[EMRConfiguration] | None = None
    LastSuccessfullyAppliedConfigurationsVersion: StrictInt | None = None
    EbsBlockDevices: list[EMREbsBlockDevice] | None = None
    EbsOptimized: StrictBool | None = None
    ShrinkPolicy: EMRShrinkPolicy | None = None
    AutoScalingPolicy: EMRAutoScalingPolicyDescription | None = None
    CustomAmiId: StrictStr | None = None
