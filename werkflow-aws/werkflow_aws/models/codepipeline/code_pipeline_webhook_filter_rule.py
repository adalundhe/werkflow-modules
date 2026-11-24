from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineWebhookFilterRule(BaseModel):
    jsonPath: StrictStr | None = None
    matchEquals: StrictStr | None = None
