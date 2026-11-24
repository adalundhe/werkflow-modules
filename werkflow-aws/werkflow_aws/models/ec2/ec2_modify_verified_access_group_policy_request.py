from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_verified_access_sse_specification_request import EC2VerifiedAccessSseSpecificationRequest


class EC2ModifyVerifiedAccessGroupPolicyRequest(BaseModel):
    VerifiedAccessGroupId: StrictStr
    PolicyEnabled: StrictBool | None = None
    PolicyDocument: StrictStr | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationRequest | None = None
