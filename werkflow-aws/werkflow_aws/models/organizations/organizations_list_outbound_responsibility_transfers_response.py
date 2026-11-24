from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_responsibility_transfer import OrganizationsResponsibilityTransfer


class OrganizationsListOutboundResponsibilityTransfersResponse(BaseModel):
    ResponsibilityTransfers: list[OrganizationsResponsibilityTransfer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
