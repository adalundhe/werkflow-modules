from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_instance_requirements_request import EC2InstanceRequirementsRequest


class EC2GetInstanceTypesFromInstanceRequirementsRequest(BaseModel):
    ArchitectureTypes: list[Literal['i386', 'x86_64', 'arm64', 'x86_64_mac', 'arm64_mac']]
    VirtualizationTypes: list[Literal['hvm', 'paravirtual']]
    InstanceRequirements: EC2InstanceRequirementsRequest
    DryRun: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Context: StrictStr | None = None
