from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_launch_template_version import EC2LaunchTemplateVersion
from .ec2_validation_warning import EC2ValidationWarning


class EC2CreateLaunchTemplateVersionResponse(BaseModel):
    LaunchTemplateVersion: EC2LaunchTemplateVersion | None = None
    Warning: EC2ValidationWarning | None = None
    ResponseMetadata: dict[str, Any] | None = None
