from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ec2_instance_requirements_request import EC2InstanceRequirementsRequest


class EC2InstanceRequirementsWithMetadataRequest(BaseModel):
    ArchitectureTypes: list[Literal['i386', 'x86_64', 'arm64', 'x86_64_mac', 'arm64_mac']] | None = None
    VirtualizationTypes: list[Literal['hvm', 'paravirtual']] | None = None
    InstanceRequirements: EC2InstanceRequirementsRequest | None = None
