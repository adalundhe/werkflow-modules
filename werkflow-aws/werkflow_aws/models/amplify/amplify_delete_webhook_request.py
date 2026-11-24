from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyDeleteWebhookRequest(BaseModel):
    webhookId: StrictStr
