from __future__ import annotations
from pydantic import BaseModel, StrictInt


class ContainerForWebhookIDs(BaseModel):
    webhookIds: list[StrictInt] | None = None
