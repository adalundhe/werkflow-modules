from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_fleet_block_device_mapping_request import EC2FleetBlockDeviceMappingRequest
from .ec2_fleet_iam_instance_profile_specification_request import EC2FleetIamInstanceProfileSpecificationRequest
from .ec2_fleet_instance_metadata_options_request import EC2FleetInstanceMetadataOptionsRequest
from .ec2_instance_requirements_request import EC2InstanceRequirementsRequest
from .ec2_placement_model import EC2PlacementModel


class EC2FleetLaunchTemplateOverridesRequest(BaseModel):
    InstanceType: StrictStr | None = None
    MaxPrice: StrictStr | None = None
    SubnetId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    WeightedCapacity: StrictFloat | StrictInt | None = None
    Priority: StrictFloat | StrictInt | None = None
    Placement: EC2PlacementModel | None = None
    KeyName: StrictStr | None = None
    BlockDeviceMappings: list[EC2FleetBlockDeviceMappingRequest] | None = None
    IamInstanceProfile: EC2FleetIamInstanceProfileSpecificationRequest | None = None
    MetadataOptions: EC2FleetInstanceMetadataOptionsRequest | None = None
    InstanceRequirements: EC2InstanceRequirementsRequest | None = None
    ImageId: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
