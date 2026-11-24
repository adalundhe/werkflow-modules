from __future__ import annotations
from pydantic import BaseModel
from .lightsail_name_servers_update_state import LightsailNameServersUpdateState
from .lightsail_r53_hosted_zone_deletion_state import LightsailR53HostedZoneDeletionState


class LightsailRegisteredDomainDelegationInfo(BaseModel):
    nameServersUpdateState: LightsailNameServersUpdateState | None = None
    r53HostedZoneDeletionState: LightsailR53HostedZoneDeletionState | None = None
