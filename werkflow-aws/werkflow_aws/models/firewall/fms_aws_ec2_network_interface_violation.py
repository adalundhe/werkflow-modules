from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSAwsEc2NetworkInterfaceViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    ViolatingSecurityGroups: list[StrictStr] | None = None
