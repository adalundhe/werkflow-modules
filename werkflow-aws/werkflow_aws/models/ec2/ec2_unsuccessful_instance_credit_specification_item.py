from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_unsuccessful_instance_credit_specification_item_error import EC2UnsuccessfulInstanceCreditSpecificationItemError


class EC2UnsuccessfulInstanceCreditSpecificationItem(BaseModel):
    InstanceId: StrictStr | None = None
    Error: EC2UnsuccessfulInstanceCreditSpecificationItemError | None = None
