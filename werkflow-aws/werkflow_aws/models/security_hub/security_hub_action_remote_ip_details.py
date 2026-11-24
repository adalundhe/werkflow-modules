from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_city import SecurityHubCity
from .security_hub_country import SecurityHubCountry
from .security_hub_geo_location import SecurityHubGeoLocation
from .security_hub_ip_organization_details import SecurityHubIpOrganizationDetails


class SecurityHubActionRemoteIpDetails(BaseModel):
    IpAddressV4: StrictStr | None = None
    Organization: SecurityHubIpOrganizationDetails | None = None
    Country: SecurityHubCountry | None = None
    City: SecurityHubCity | None = None
    GeoLocation: SecurityHubGeoLocation | None = None
