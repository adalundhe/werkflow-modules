from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_domain_entry import LightsailDomainEntry
from .lightsail_registered_domain_delegation_info import LightsailRegisteredDomainDelegationInfo
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailDomain(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    domainEntries: list[LightsailDomainEntry] | None = None
    registeredDomainDelegationInfo: LightsailRegisteredDomainDelegationInfo | None = None
