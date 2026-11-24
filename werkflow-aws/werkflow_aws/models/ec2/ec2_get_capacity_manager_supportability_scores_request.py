from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_instance_requirements_with_metadata_request import EC2InstanceRequirementsWithMetadataRequest


class EC2GetCapacityManagerSupportabilityScoresRequest(BaseModel):
    MarketType: Literal['on-demand', 'spot']
    CapacityAmount: StrictInt
    CapacityUnit: Literal['vcpus', 'instances']
    CapacityAvailabilityZoneIds: list[StrictStr]
    InstanceTypes: list[StrictStr] | None = None
    InstanceRequirementsWithMetadata: EC2InstanceRequirementsWithMetadataRequest | None = None
    DryRun: StrictBool | None = None
