from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_webhook import AmplifyWebhook


class AmplifyCreateWebhookResponse(BaseModel):
    webhook: AmplifyWebhook | None = None
    ResponseMetadata: dict[str, Any] | None = None
