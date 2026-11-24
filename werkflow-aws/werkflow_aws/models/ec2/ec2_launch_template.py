from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_operator_response import EC2OperatorResponse
from .ec2_tag_model import EC2TagModel


class EC2LaunchTemplate(BaseModel):
    LaunchTemplateId: StrictStr | None = None
    LaunchTemplateName: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    DefaultVersionNumber: StrictInt | None = None
    LatestVersionNumber: StrictInt | None = None
    Tags: list[EC2TagModel] | None = None
    Operator: EC2OperatorResponse | None = None
