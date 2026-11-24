from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EC2LaunchTemplateEnclaveOptionsRequest(BaseModel):
    Enabled: StrictBool | None = None
