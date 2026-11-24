from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_operator_response import EC2OperatorResponse
from .ec2_response_launch_template_data import EC2ResponseLaunchTemplateData


class EC2LaunchTemplateVersion(BaseModel):
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    VersionNumber: StrictInt | None = None
    VersionDescription: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    DefaultVersion: StrictBool | None = None
    LaunchTemplateData: EC2ResponseLaunchTemplateData | None = None
    Operator: EC2OperatorResponse | None = None
