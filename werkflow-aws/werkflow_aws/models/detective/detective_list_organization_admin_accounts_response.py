from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .detective_administrator import DetectiveAdministrator


class DetectiveListOrganizationAdminAccountsResponse(BaseModel):
    Administrators: list[DetectiveAdministrator] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
