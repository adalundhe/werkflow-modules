from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_verified_access_log_options import EC2VerifiedAccessLogOptions


class EC2ModifyVerifiedAccessInstanceLoggingConfigurationRequest(BaseModel):
    VerifiedAccessInstanceId: StrictStr
    AccessLogs: EC2VerifiedAccessLogOptions
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
