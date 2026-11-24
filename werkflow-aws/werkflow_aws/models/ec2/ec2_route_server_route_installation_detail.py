from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2RouteServerRouteInstallationDetail(BaseModel):
    RouteTableId: StrictStr | None = None
    RouteInstallationStatus: StrictStr | None = None
    RouteInstallationStatusReason: StrictStr | None = None
