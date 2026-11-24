from __future__ import annotations
from pydantic import BaseModel, StrictInt


class WebhooksExpirationDate(BaseModel):
    expirationDate: StrictInt | None = None
