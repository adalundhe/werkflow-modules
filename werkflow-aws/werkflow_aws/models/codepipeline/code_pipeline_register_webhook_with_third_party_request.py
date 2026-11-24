from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineRegisterWebhookWithThirdPartyRequest(BaseModel):
    webhookName: StrictStr | None = None
