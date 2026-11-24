from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_successful_suppression_response_object import EC2SuccessfulSuppressionResponseObject
from .ec2_unsuccessful_suppression_response_object import EC2UnsuccessfulSuppressionResponseObject


class EC2EnableApplicationStatusCheckSuppressionResponse(BaseModel):
    SuccessfulResults: list[EC2SuccessfulSuppressionResponseObject] | None = None
    UnsuccessfulResults: list[EC2UnsuccessfulSuppressionResponseObject] | None = None
    ResponseMetadata: dict[str, Any] | None = None
