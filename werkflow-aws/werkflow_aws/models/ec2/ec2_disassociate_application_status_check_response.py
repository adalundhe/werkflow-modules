from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_successful_association_response_object import EC2SuccessfulAssociationResponseObject
from .ec2_unsuccessful_association_response_object import EC2UnsuccessfulAssociationResponseObject


class EC2DisassociateApplicationStatusCheckResponse(BaseModel):
    SuccessfulResults: list[EC2SuccessfulAssociationResponseObject] | None = None
    UnsuccessfulResults: list[EC2UnsuccessfulAssociationResponseObject] | None = None
    ResponseMetadata: dict[str, Any] | None = None
