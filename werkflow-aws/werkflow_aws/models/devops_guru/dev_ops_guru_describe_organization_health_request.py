from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DevOpsGuruDescribeOrganizationHealthRequest(BaseModel):
    AccountIds: list[StrictStr] | None = None
    OrganizationalUnitIds: list[StrictStr] | None = None
