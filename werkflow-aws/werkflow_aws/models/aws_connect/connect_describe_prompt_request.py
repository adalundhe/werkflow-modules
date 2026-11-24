from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribePromptRequest(BaseModel):
    InstanceId: StrictStr
    PromptId: StrictStr
