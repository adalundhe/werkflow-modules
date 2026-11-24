from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTStepFunctionsAction(BaseModel):
    executionNamePrefix: StrictStr | None = None
    stateMachineName: StrictStr | None = None
    roleArn: StrictStr | None = None
