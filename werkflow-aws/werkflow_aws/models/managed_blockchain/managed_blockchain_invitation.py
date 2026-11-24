from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .managed_blockchain_network_summary import ManagedBlockchainNetworkSummary


class ManagedBlockchainInvitation(BaseModel):
    InvitationId: StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
    ExpirationDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    NetworkSummary: ManagedBlockchainNetworkSummary | None = None
    Arn: StrictStr | None = None
