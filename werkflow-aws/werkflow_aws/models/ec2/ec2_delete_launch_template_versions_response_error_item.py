from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_response_error import EC2ResponseError


class EC2DeleteLaunchTemplateVersionsResponseErrorItem(BaseModel):
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    ResponseError: EC2ResponseError | None = None
