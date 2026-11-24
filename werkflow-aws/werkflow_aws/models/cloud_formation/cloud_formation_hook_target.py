from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationHookTarget(BaseModel):
    TargetType: StrictStr | None = None
    TargetTypeName: StrictStr | None = None
    TargetId: StrictStr | None = None
    Action: StrictStr | None = None
