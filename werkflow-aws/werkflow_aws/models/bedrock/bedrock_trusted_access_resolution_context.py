from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockTrustedAccessResolutionContext(BaseModel):
    accountId: StrictStr | None = None
    projectArn: StrictStr | None = None
