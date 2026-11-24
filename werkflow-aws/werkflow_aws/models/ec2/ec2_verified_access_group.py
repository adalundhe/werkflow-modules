from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_verified_access_sse_specification_response import EC2VerifiedAccessSseSpecificationResponse


class EC2VerifiedAccessGroup(BaseModel):
    VerifiedAccessGroupId: StrictStr | None = None
    VerifiedAccessInstanceId: StrictStr | None = None
    Description: StrictStr | None = None
    Owner: StrictStr | None = None
    VerifiedAccessGroupArn: StrictStr | None = None
    CreationTime: StrictStr | None = None
    LastUpdatedTime: StrictStr | None = None
    DeletionTime: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    SseSpecification: EC2VerifiedAccessSseSpecificationResponse | None = None
