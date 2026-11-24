from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_spot_instance_state_fault import EC2SpotInstanceStateFault


class EC2SpotDatafeedSubscription(BaseModel):
    Bucket: StrictStr | None = None
    Fault: EC2SpotInstanceStateFault | None = None
    OwnerId: StrictStr | None = None
    Prefix: StrictStr | None = None
    State: StrictStr | None = None
