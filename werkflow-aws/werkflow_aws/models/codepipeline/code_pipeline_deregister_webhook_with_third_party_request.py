from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineDeregisterWebhookWithThirdPartyRequest(BaseModel):
    webhookName: StrictStr | None = None
