from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_verified_access_sse_specification_request import EC2VerifiedAccessSseSpecificationRequest


class EC2CreateVerifiedAccessGroupRequest(BaseModel):
    VerifiedAccessInstanceId: StrictStr
    Description: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationRequest | None = None
