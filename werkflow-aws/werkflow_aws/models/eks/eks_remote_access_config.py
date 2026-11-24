from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSRemoteAccessConfig(BaseModel):
    ec2SshKey: StrictStr | None = None
    sourceSecurityGroups: list[StrictStr] | None = None
