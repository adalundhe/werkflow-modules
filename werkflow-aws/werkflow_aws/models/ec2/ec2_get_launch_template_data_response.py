from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_response_launch_template_data import EC2ResponseLaunchTemplateData


class EC2GetLaunchTemplateDataResponse(BaseModel):
    LaunchTemplateData: EC2ResponseLaunchTemplateData | None = None
    ResponseMetadata: dict[str, Any] | None = None
