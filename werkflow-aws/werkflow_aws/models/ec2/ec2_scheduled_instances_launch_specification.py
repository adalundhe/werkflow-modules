from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_scheduled_instances_block_device_mapping import EC2ScheduledInstancesBlockDeviceMapping
from .ec2_scheduled_instances_iam_instance_profile import EC2ScheduledInstancesIamInstanceProfile
from .ec2_scheduled_instances_monitoring import EC2ScheduledInstancesMonitoring
from .ec2_scheduled_instances_network_interface import EC2ScheduledInstancesNetworkInterface
from .ec2_scheduled_instances_placement import EC2ScheduledInstancesPlacement


class EC2ScheduledInstancesLaunchSpecification(BaseModel):
    ImageId: StrictStr
    BlockDeviceMappings: list[EC2ScheduledInstancesBlockDeviceMapping] | None = None
    EbsOptimized: StrictBool | None = None
    IamInstanceProfile: EC2ScheduledInstancesIamInstanceProfile | None = None
    InstanceType: StrictStr | None = None
    KernelId: StrictStr | None = None
    KeyName: StrictStr | None = None
    Monitoring: EC2ScheduledInstancesMonitoring | None = None
    NetworkInterfaces: list[EC2ScheduledInstancesNetworkInterface] | None = None
    Placement: EC2ScheduledInstancesPlacement | None = None
    RamdiskId: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    SubnetId: StrictStr | None = None
    UserData: StrictStr | None = None
