from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexQInConnectAssistantConfiguration(BaseModel):
    assistantArn: StrictStr | None = None
