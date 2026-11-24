from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2BedrockGuardrailsRequestOnly(BaseModel):
    RoleArn: StrictStr | None = None
