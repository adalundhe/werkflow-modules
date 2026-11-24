from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRExecutionEngineConfig(BaseModel):
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    MasterInstanceSecurityGroupId: StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
