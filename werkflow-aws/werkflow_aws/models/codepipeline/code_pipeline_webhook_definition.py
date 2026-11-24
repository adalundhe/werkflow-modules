from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_webhook_auth_configuration import CodePipelineWebhookAuthConfiguration
from .code_pipeline_webhook_filter_rule import CodePipelineWebhookFilterRule


class CodePipelineWebhookDefinition(BaseModel):
    name: StrictStr | None = None
    targetPipeline: StrictStr | None = None
    targetAction: StrictStr | None = None
    filters: list[CodePipelineWebhookFilterRule] | None = None
    authentication: StrictStr | None = None
    authenticationConfiguration: CodePipelineWebhookAuthConfiguration | None = None
