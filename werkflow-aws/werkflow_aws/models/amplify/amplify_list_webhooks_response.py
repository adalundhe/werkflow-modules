from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amplify_webhook import AmplifyWebhook


class AmplifyListWebhooksResponse(BaseModel):
    webhooks: list[AmplifyWebhook] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
