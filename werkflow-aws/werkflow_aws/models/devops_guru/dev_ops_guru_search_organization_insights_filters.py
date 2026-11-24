from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .dev_ops_guru_resource_collection import DevOpsGuruResourceCollection
from .dev_ops_guru_service_collection import DevOpsGuruServiceCollection


class DevOpsGuruSearchOrganizationInsightsFilters(BaseModel):
    Severities: list[Literal['LOW', 'MEDIUM', 'HIGH']] | None = None
    Statuses: list[Literal['ONGOING', 'CLOSED']] | None = None
    ResourceCollection: DevOpsGuruResourceCollection | None = None
    ServiceCollection: DevOpsGuruServiceCollection | None = None
