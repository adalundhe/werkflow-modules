from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .organizations_transfer_participant import OrganizationsTransferParticipant


class OrganizationsResponsibilityTransfer(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    Source: OrganizationsTransferParticipant | None = None
    Target: OrganizationsTransferParticipant | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    EndTimestamp: datetime.datetime | StrictStr | None = None
    ActiveHandshakeId: StrictStr | None = None
