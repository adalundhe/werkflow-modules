from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_operator_request import EC2OperatorRequest
from .ec2_request_launch_template_data import EC2RequestLaunchTemplateData
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateLaunchTemplateRequest(BaseModel):
    LaunchTemplateName: StrictStr
    LaunchTemplateData: EC2RequestLaunchTemplateData
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    VersionDescription: StrictStr | None = None
    Operator: EC2OperatorRequest | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
