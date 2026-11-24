from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectGetPromptFileRequest(BaseModel):
    InstanceId: StrictStr
    PromptId: StrictStr
