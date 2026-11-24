from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraSaaSConfiguration(BaseModel):
    OrganizationName: StrictStr | None = None
    HostUrl: StrictStr | None = None
