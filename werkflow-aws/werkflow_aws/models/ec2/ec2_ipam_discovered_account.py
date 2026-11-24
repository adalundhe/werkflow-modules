from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_ipam_discovery_failure_reason import EC2IpamDiscoveryFailureReason


class EC2IpamDiscoveredAccount(BaseModel):
    AccountId: StrictStr | None = None
    DiscoveryRegion: StrictStr | None = None
    FailureReason: EC2IpamDiscoveryFailureReason | None = None
    LastAttemptedDiscoveryTime: datetime.datetime | StrictStr | None = None
    LastSuccessfulDiscoveryTime: datetime.datetime | StrictStr | None = None
    OrganizationalUnitId: StrictStr | None = None
