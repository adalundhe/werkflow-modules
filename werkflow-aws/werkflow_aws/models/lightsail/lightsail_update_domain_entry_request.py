from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_domain_entry import LightsailDomainEntry


class LightsailUpdateDomainEntryRequest(BaseModel):
    domainName: StrictStr
    domainEntry: LightsailDomainEntry
