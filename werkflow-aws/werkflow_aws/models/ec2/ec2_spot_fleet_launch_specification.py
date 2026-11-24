from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .ec2_block_device_mapping import EC2BlockDeviceMapping
from .ec2_group_identifier_model import EC2GroupIdentifierModel
from .ec2_iam_instance_profile_specification import EC2IamInstanceProfileSpecification
from .ec2_instance_network_interface_specification import EC2InstanceNetworkInterfaceSpecification
from .ec2_instance_requirements import EC2InstanceRequirements
from .ec2_spot_fleet_monitoring import EC2SpotFleetMonitoring
from .ec2_spot_fleet_tag_specification import EC2SpotFleetTagSpecification
from .ec2_spot_placement import EC2SpotPlacement


class EC2SpotFleetLaunchSpecification(BaseModel):
    AddressingType: StrictStr | None = None
    BlockDeviceMappings: list[EC2BlockDeviceMapping] | None = None
    EbsOptimized: StrictBool | None = None
    IamInstanceProfile: EC2IamInstanceProfileSpecification | None = None
    ImageId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    KernelId: StrictStr | None = None
    KeyName: StrictStr | None = None
    Monitoring: EC2SpotFleetMonitoring | None = None
    NetworkInterfaces: list[EC2InstanceNetworkInterfaceSpecification] | None = None
    Placement: EC2SpotPlacement | None = None
    RamdiskId: StrictStr | None = None
    SpotPrice: StrictStr | None = None
    SubnetId: StrictStr | None = None
    UserData: StrictStr | None = None
    WeightedCapacity: StrictFloat | StrictInt | None = None
    TagSpecifications: list[EC2SpotFleetTagSpecification] | None = None
    InstanceRequirements: EC2InstanceRequirements | None = None
    SecurityGroups: list[EC2GroupIdentifierModel] | None = None
