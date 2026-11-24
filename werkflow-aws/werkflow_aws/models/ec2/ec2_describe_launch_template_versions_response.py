from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_launch_template_version import EC2LaunchTemplateVersion


class EC2DescribeLaunchTemplateVersionsResponse(BaseModel):
    LaunchTemplateVersions: list[EC2LaunchTemplateVersion] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
