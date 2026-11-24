from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_tag import CodePipelineTag
from .code_pipeline_webhook_definition import CodePipelineWebhookDefinition


class CodePipelinePutWebhookRequest(BaseModel):
    webhook: CodePipelineWebhookDefinition
    tags: list[CodePipelineTag] | None = None
