from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_successful_instance_credit_specification_item import EC2SuccessfulInstanceCreditSpecificationItem
from .ec2_unsuccessful_instance_credit_specification_item import EC2UnsuccessfulInstanceCreditSpecificationItem


class EC2ModifyInstanceCreditSpecificationResponse(BaseModel):
    SuccessfulInstanceCreditSpecifications: list[EC2SuccessfulInstanceCreditSpecificationItem] | None = None
    UnsuccessfulInstanceCreditSpecifications: list[EC2UnsuccessfulInstanceCreditSpecificationItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
