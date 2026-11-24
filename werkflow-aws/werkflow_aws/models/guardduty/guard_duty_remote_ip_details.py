from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_city import GuardDutyCity
from .guard_duty_country import GuardDutyCountry
from .guard_duty_geo_location import GuardDutyGeoLocation
from .guard_duty_organization import GuardDutyOrganization


class GuardDutyRemoteIpDetails(BaseModel):
    City: GuardDutyCity | None = None
    Country: GuardDutyCountry | None = None
    GeoLocation: GuardDutyGeoLocation | None = None
    IpAddressV4: StrictStr | None = None
    IpAddressV6: StrictStr | None = None
    Organization: GuardDutyOrganization | None = None
