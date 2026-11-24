from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_blockchain_node_log_publishing_configuration import ManagedBlockchainNodeLogPublishingConfiguration


class ManagedBlockchainUpdateNodeRequest(BaseModel):
    NetworkId: StrictStr
    NodeId: StrictStr
    MemberId: StrictStr | None = None
    LogPublishingConfiguration: ManagedBlockchainNodeLogPublishingConfiguration | None = None
