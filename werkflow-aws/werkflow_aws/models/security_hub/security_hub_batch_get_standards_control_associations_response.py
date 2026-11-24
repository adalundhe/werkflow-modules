from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_hub_standards_control_association_detail import SecurityHubStandardsControlAssociationDetail
from .security_hub_unprocessed_standards_control_association import SecurityHubUnprocessedStandardsControlAssociation


class SecurityHubBatchGetStandardsControlAssociationsResponse(BaseModel):
    StandardsControlAssociationDetails: list[SecurityHubStandardsControlAssociationDetail] | None = None
    UnprocessedAssociations: list[SecurityHubUnprocessedStandardsControlAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
