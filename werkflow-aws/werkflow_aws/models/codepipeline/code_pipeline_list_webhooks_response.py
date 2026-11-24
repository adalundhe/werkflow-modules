from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_list_webhook_item import CodePipelineListWebhookItem


class CodePipelineListWebhooksResponse(BaseModel):
    webhooks: list[CodePipelineListWebhookItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
