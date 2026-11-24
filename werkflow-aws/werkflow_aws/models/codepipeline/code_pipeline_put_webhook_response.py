from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_list_webhook_item import CodePipelineListWebhookItem


class CodePipelinePutWebhookResponse(BaseModel):
    webhook: CodePipelineListWebhookItem | None = None
    ResponseMetadata: dict[str, Any] | None = None
