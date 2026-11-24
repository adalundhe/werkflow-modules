from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsTransferParticipant(BaseModel):
    ManagementAccountId: StrictStr | None = None
    ManagementAccountEmail: StrictStr | None = None
