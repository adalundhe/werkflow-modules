from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildDeleteWebhookRequest(BaseModel):
    projectName: StrictStr
