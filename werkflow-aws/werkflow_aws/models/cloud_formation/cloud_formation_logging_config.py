from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationLoggingConfig(BaseModel):
    LogRoleArn: StrictStr | None = None
    LogGroupName: StrictStr | None = None
