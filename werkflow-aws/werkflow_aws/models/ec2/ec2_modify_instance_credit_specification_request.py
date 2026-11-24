from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_instance_credit_specification_request import EC2InstanceCreditSpecificationRequest


class EC2ModifyInstanceCreditSpecificationRequest(BaseModel):
    InstanceCreditSpecifications: list[EC2InstanceCreditSpecificationRequest]
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
