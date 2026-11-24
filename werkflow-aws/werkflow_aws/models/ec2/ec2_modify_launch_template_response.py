from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_launch_template import EC2LaunchTemplate


class EC2ModifyLaunchTemplateResponse(BaseModel):
    LaunchTemplate: EC2LaunchTemplate | None = None
    ResponseMetadata: dict[str, Any] | None = None
