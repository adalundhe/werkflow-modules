from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .managed_grafana_authentication_summary import ManagedGrafanaAuthenticationSummary


class ManagedGrafanaWorkspaceSummary(BaseModel):
    created: datetime.datetime | StrictStr | None = None
    description: StrictStr | None = None
    endpoint: StrictStr | None = None
    grafanaVersion: StrictStr | None = None
    id: StrictStr | None = None
    modified: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    notificationDestinations: list[StrictStr] | None = None
    status: StrictStr | None = None
    authentication: ManagedGrafanaAuthenticationSummary | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    licenseType: StrictStr | None = None
    grafanaToken: StrictStr | None = None
