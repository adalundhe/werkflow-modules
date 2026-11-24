from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_launch_template import EC2LaunchTemplate
from .ec2_validation_warning import EC2ValidationWarning


class EC2CreateLaunchTemplateResponse(BaseModel):
    LaunchTemplate: EC2LaunchTemplate | None = None
    Warning: EC2ValidationWarning | None = None
    ResponseMetadata: dict[str, Any] | None = None
