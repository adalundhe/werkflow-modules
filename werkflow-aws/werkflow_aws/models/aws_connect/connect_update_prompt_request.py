from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdatePromptRequest(BaseModel):
    InstanceId: StrictStr
    PromptId: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    S3Uri: StrictStr | None = None
