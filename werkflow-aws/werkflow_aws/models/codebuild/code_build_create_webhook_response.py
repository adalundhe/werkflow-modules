from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_webhook import CodeBuildWebhook


class CodeBuildCreateWebhookResponse(BaseModel):
    webhook: CodeBuildWebhook | None = None
    ResponseMetadata: dict[str, Any] | None = None
