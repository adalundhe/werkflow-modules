from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .webhook_details import WebhookDetails


class WebhookRegistrationDetails(BaseModel):
    url: StrictStr | None = None
    webhooks: list[WebhookDetails] | None = None
