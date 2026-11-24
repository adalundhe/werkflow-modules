from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_delete_launch_template_versions_response_error_item import EC2DeleteLaunchTemplateVersionsResponseErrorItem
from .ec2_delete_launch_template_versions_response_success_item import EC2DeleteLaunchTemplateVersionsResponseSuccessItem


class EC2DeleteLaunchTemplateVersionsResponse(BaseModel):
    SuccessfullyDeletedLaunchTemplateVersions: list[EC2DeleteLaunchTemplateVersionsResponseSuccessItem] | None = None
    UnsuccessfullyDeletedLaunchTemplateVersions: list[EC2DeleteLaunchTemplateVersionsResponseErrorItem] | None = None
    ResponseMetadata: dict[str, Any] | None = None
