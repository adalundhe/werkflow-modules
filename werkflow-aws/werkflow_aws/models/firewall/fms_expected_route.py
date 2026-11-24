from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSExpectedRoute(BaseModel):
    IpV4Cidr: StrictStr | None = None
    PrefixListId: StrictStr | None = None
    IpV6Cidr: StrictStr | None = None
    ContributingSubnets: list[StrictStr] | None = None
    AllowedTargets: list[StrictStr] | None = None
    RouteTableId: StrictStr | None = None
