from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_instance_credit_specification import EC2InstanceCreditSpecification


class EC2DescribeInstanceCreditSpecificationsResponse(BaseModel):
    InstanceCreditSpecifications: list[EC2InstanceCreditSpecification] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
