from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGetPromptRouterRequest(BaseModel):
    promptRouterArn: StrictStr
