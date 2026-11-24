from __future__ import annotations
from pydantic import BaseModel, StrictBool


class MacieSecurityHubConfiguration(BaseModel):
    publishClassificationFindings: StrictBool | None = None
    publishPolicyFindings: StrictBool | None = None
