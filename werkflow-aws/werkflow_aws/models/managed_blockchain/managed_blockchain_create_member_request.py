from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_blockchain_member_configuration import ManagedBlockchainMemberConfiguration


class ManagedBlockchainCreateMemberRequest(BaseModel):
    ClientRequestToken: StrictStr
    InvitationId: StrictStr
    NetworkId: StrictStr
    MemberConfiguration: ManagedBlockchainMemberConfiguration
