from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_unprocessed_standards_control_association_update import SecurityHubUnprocessedStandardsControlAssociationUpdate


class SecurityHubBatchUpdateStandardsControlAssociationsResponse(BaseModel):
    UnprocessedAssociationUpdates: list[SecurityHubUnprocessedStandardsControlAssociationUpdate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
