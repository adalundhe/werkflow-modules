from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataIamInstanceProfileDetails(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
