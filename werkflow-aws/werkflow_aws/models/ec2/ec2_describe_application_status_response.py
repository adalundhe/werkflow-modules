from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_application_statuses_response_type import EC2ApplicationStatusesResponseType


class EC2DescribeApplicationStatusResponse(BaseModel):
    ApplicationStatuses: EC2ApplicationStatusesResponseType | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
