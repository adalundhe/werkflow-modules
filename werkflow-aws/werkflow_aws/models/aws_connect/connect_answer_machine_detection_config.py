from __future__ import annotations
from pydantic import BaseModel, StrictBool


class ConnectAnswerMachineDetectionConfig(BaseModel):
    EnableAnswerMachineDetection: StrictBool | None = None
    AwaitAnswerMachinePrompt: StrictBool | None = None
