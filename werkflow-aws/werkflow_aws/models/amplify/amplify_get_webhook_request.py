from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyGetWebhookRequest(BaseModel):
    webhookId: StrictStr
