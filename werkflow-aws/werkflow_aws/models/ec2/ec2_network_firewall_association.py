from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2NetworkFirewallAssociation(BaseModel):
    FirewallArn: StrictStr | None = None
    FirewallOnboardingStatus: StrictStr | None = None
    FirewallMode: StrictStr | None = None
