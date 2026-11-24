from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_application_status_check_response_object import EC2ApplicationStatusCheckResponseObject


class EC2DescribeApplicationStatusChecksResponse(BaseModel):
    ApplicationStatusChecks: list[EC2ApplicationStatusCheckResponseObject] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
