from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_blockchain_member_log_publishing_configuration import ManagedBlockchainMemberLogPublishingConfiguration


class ManagedBlockchainUpdateMemberRequest(BaseModel):
    NetworkId: StrictStr
    MemberId: StrictStr
    LogPublishingConfiguration: ManagedBlockchainMemberLogPublishingConfiguration | None = None
