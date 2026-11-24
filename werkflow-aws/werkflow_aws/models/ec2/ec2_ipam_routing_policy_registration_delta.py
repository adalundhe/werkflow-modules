from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamRoutingPolicyRegistrationDelta(BaseModel):
    DeltaId: StrictStr | None = None
    DeltaJson: StrictStr | None = None
    State: StrictStr | None = None
    StateMessage: StrictStr | None = None
