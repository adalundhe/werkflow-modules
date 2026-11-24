from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_responsibility_transfer import OrganizationsResponsibilityTransfer


class OrganizationsTerminateResponsibilityTransferResponse(BaseModel):
    ResponsibilityTransfer: OrganizationsResponsibilityTransfer | None = None
    ResponseMetadata: dict[str, Any] | None = None
