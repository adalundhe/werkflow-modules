from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_request_launch_template_data import EC2RequestLaunchTemplateData


class EC2CreateLaunchTemplateVersionRequest(BaseModel):
    LaunchTemplateData: EC2RequestLaunchTemplateData
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    SourceVersion: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    ResolveAlias: StrictBool | None = None
