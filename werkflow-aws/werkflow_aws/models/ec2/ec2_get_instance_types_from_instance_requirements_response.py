from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_type_info_from_instance_requirements import EC2InstanceTypeInfoFromInstanceRequirements


class EC2GetInstanceTypesFromInstanceRequirementsResponse(BaseModel):
    InstanceTypes: list[EC2InstanceTypeInfoFromInstanceRequirements] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
