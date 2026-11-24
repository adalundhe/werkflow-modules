from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_standards_control_association_id import SecurityHubStandardsControlAssociationId


class SecurityHubUnprocessedStandardsControlAssociation(BaseModel):
    StandardsControlAssociationId: SecurityHubStandardsControlAssociationId | None = None
    ErrorCode: StrictStr | None = None
    ErrorReason: StrictStr | None = None
