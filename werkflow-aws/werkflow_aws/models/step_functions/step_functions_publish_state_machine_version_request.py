from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StepFunctionsPublishStateMachineVersionRequest(BaseModel):
    stateMachineArn: StrictStr
    revisionId: StrictStr | None = None
    description: StrictStr | None = None
