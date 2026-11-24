from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_application_status_check_response_object import EC2ApplicationStatusCheckResponseObject


class EC2ModifyApplicationStatusCheckResponse(BaseModel):
    ApplicationStatusCheck: EC2ApplicationStatusCheckResponseObject | None = None
    ResponseMetadata: dict[str, Any] | None = None
