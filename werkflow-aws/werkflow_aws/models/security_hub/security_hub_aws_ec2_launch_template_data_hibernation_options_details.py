from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsEc2LaunchTemplateDataHibernationOptionsDetails(BaseModel):
    Configured: StrictBool | None = None
