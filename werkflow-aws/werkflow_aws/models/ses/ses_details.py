from __future__ import annotations
from pydantic import BaseModel
from .ses_route_details import SESRouteDetails


class SESDetails(BaseModel):
    RoutesDetails: list[SESRouteDetails]
