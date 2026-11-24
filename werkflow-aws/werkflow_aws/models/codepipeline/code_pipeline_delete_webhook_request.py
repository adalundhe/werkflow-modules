from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineDeleteWebhookRequest(BaseModel):
    name: StrictStr
