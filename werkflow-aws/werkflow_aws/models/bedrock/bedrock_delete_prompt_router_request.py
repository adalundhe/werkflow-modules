from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDeletePromptRouterRequest(BaseModel):
    promptRouterArn: StrictStr
