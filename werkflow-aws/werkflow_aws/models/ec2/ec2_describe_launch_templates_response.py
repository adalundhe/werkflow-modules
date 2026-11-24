from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_launch_template import EC2LaunchTemplate


class EC2DescribeLaunchTemplatesResponse(BaseModel):
    LaunchTemplates: list[EC2LaunchTemplate] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
