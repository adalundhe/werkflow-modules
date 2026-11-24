from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_logs import EC2VerifiedAccessLogs


class EC2VerifiedAccessInstanceLoggingConfiguration(BaseModel):
    VerifiedAccessInstanceId: StrictStr | None = None
    AccessLogs: EC2VerifiedAccessLogs | None = None
