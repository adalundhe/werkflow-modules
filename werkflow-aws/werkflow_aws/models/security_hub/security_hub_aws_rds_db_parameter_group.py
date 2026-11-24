from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsDbParameterGroup(BaseModel):
    DbParameterGroupName: StrictStr | None = None
    ParameterApplyStatus: StrictStr | None = None
