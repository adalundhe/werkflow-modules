from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OrganizationsEnabledServicePrincipal(BaseModel):
    ServicePrincipal: StrictStr | None = None
    DateEnabled: datetime.datetime | StrictStr | None = None
