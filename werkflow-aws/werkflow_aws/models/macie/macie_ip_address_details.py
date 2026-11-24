from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_ip_city import MacieIpCity
from .macie_ip_country import MacieIpCountry
from .macie_ip_geo_location import MacieIpGeoLocation
from .macie_ip_owner import MacieIpOwner


class MacieIpAddressDetails(BaseModel):
    ipAddressV4: StrictStr | None = None
    ipCity: MacieIpCity | None = None
    ipCountry: MacieIpCountry | None = None
    ipGeoLocation: MacieIpGeoLocation | None = None
    ipOwner: MacieIpOwner | None = None
