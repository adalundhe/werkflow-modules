from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineWebhookAuthConfiguration(BaseModel):
    AllowedIPRange: StrictStr | None = None
    SecretToken: StrictStr | None = None
