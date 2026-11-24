from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RegisteredWebhook(BaseModel):
    createdWebhookId: StrictInt | None = None
    errors: list[StrictStr] | None = None
