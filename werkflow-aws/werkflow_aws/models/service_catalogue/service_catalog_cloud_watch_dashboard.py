from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogCloudWatchDashboard(BaseModel):
    Name: StrictStr | None = None
