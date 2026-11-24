from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreatePromptRequest(BaseModel):
    InstanceId: StrictStr
    Name: StrictStr
    S3Uri: StrictStr
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
