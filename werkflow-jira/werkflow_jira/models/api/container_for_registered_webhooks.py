from __future__ import annotations
from pydantic import BaseModel
from .registered_webhook import RegisteredWebhook


class ContainerForRegisteredWebhooks(BaseModel):
    webhookRegistrationResult: list[RegisteredWebhook] | None = None
