from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_project_grant_filter import DataZoneProjectGrantFilter


class DataZoneProjectPolicyGrantPrincipal(BaseModel):
    projectDesignation: StrictStr | None = None
    userCreatedDesignationId: StrictStr | None = None
    projectIdentifier: StrictStr | None = None
    projectGrantFilter: DataZoneProjectGrantFilter | None = None
