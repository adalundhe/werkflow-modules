from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_standards_control_association_update import SecurityHubStandardsControlAssociationUpdate


class SecurityHubUnprocessedStandardsControlAssociationUpdate(BaseModel):
    StandardsControlAssociationUpdate: SecurityHubStandardsControlAssociationUpdate | None = None
    ErrorCode: StrictStr | None = None
    ErrorReason: StrictStr | None = None
