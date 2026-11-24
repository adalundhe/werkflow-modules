from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockPromptRouterTargetModel(BaseModel):
    modelArn: StrictStr | None = None
