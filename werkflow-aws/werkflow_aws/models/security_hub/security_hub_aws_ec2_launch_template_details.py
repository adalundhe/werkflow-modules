from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_ec2_launch_template_data_details import SecurityHubAwsEc2LaunchTemplateDataDetails


class SecurityHubAwsEc2LaunchTemplateDetails(BaseModel):
    LaunchTemplateName: StrictStr | None = None
    Id: StrictStr | None = None
    LaunchTemplateData: SecurityHubAwsEc2LaunchTemplateDataDetails | None = None
    DefaultVersionNumber: StrictInt | None = None
    LatestVersionNumber: StrictInt | None = None
