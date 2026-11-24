from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyUpdateWebhookRequest(BaseModel):
    webhookId: StrictStr
    branchName: StrictStr | None = None
    description: StrictStr | None = None
