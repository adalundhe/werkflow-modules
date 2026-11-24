from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildWebhookFilter(BaseModel):
    type: StrictStr | None = None
    pattern: StrictStr | None = None
    excludeMatchedPattern: StrictBool | None = None
