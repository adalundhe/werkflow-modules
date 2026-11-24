from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OrganizationsDelegatedService(BaseModel):
    ServicePrincipal: StrictStr | None = None
    DelegationEnabledDate: datetime.datetime | StrictStr | None = None
