from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSThirdPartyFirewallPolicy(BaseModel):
    FirewallDeploymentModel: StrictStr | None = None
