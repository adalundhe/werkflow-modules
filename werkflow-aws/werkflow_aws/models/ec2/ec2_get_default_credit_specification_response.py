from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_instance_family_credit_specification import EC2InstanceFamilyCreditSpecification


class EC2GetDefaultCreditSpecificationResponse(BaseModel):
    InstanceFamilyCreditSpecification: EC2InstanceFamilyCreditSpecification | None = None
    ResponseMetadata: dict[str, Any] | None = None
