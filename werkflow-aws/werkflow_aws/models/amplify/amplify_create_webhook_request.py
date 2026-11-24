from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyCreateWebhookRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    description: StrictStr | None = None
