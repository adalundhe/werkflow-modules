from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .failed_webhook import FailedWebhook


class FailedWebhooks(BaseModel):
    maxResults: StrictInt | None = None
    next: StrictStr | None = None
    values: list[FailedWebhook] | None = None
