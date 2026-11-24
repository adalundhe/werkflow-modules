from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationGetHookResultRequest(BaseModel):
    HookResultId: StrictStr | None = None
