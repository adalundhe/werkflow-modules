from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_domain_maintenance_details import OpenSearchDomainMaintenanceDetails


class OpenSearchListDomainMaintenancesResponse(BaseModel):
    DomainMaintenances: list[OpenSearchDomainMaintenanceDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
