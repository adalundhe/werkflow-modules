from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_pipeline_tag import CodePipelineTag
from .code_pipeline_webhook_definition import CodePipelineWebhookDefinition


class CodePipelineListWebhookItem(BaseModel):
    definition: CodePipelineWebhookDefinition | None = None
    url: StrictStr | None = None
    errorMessage: StrictStr | None = None
    errorCode: StrictStr | None = None
    lastTriggered: datetime.datetime | StrictStr | None = None
    arn: StrictStr | None = None
    tags: list[CodePipelineTag] | None = None
