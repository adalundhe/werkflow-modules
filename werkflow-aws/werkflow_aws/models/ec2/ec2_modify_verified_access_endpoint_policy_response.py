from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_verified_access_sse_specification_response import EC2VerifiedAccessSseSpecificationResponse


class EC2ModifyVerifiedAccessEndpointPolicyResponse(BaseModel):
    PolicyEnabled: StrictBool | None = None
    PolicyDocument: StrictStr | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
