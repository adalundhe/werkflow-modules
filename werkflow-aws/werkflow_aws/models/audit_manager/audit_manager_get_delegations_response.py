from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_delegation_metadata import AuditManagerDelegationMetadata


class AuditManagerGetDelegationsResponse(BaseModel):
    delegations: list[AuditManagerDelegationMetadata] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
