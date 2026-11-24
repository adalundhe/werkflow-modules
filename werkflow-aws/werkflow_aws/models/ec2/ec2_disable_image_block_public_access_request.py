from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2DisableImageBlockPublicAccessRequest(BaseModel):
    DryRun: StrictBool | None = None
