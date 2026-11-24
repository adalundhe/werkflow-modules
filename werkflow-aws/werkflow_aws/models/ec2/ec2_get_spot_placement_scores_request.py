from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_instance_requirements_with_metadata_request import EC2InstanceRequirementsWithMetadataRequest


class EC2GetSpotPlacementScoresRequest(BaseModel):
    TargetCapacity: StrictInt
    InstanceTypes: list[StrictStr] | None = None
    TargetCapacityUnitType: Literal['vcpu', 'memory-mib', 'units'] | None = None
    SingleAvailabilityZone: StrictBool | None = None
    RegionNames: list[StrictStr] | None = None
    InstanceRequirementsWithMetadata: EC2InstanceRequirementsWithMetadataRequest | None = None
    DryRun: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    IncludeLocalZones: StrictBool | None = None
