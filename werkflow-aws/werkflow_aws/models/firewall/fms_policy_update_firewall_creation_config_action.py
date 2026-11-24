from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSPolicyUpdateFirewallCreationConfigAction(BaseModel):
    Description: StrictStr | None = None
    FirewallCreationConfig: StrictStr | None = None
