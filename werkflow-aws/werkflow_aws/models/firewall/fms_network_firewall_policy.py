from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSNetworkFirewallPolicy(BaseModel):
    FirewallDeploymentModel: StrictStr | None = None
