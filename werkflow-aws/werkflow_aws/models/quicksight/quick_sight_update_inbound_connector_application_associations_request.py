from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateInboundConnectorApplicationAssociationsRequest(BaseModel):
    AwsAccountId: StrictStr
    InboundConnectorId: StrictStr
    AssociateAccessControlApplications: list[StrictStr] | None = None
    DisassociateAccessControlApplications: list[StrictStr] | None = None
