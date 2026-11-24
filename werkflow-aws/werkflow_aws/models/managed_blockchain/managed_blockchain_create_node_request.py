from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_blockchain_node_configuration import ManagedBlockchainNodeConfiguration


class ManagedBlockchainCreateNodeRequest(BaseModel):
    ClientRequestToken: StrictStr
    NetworkId: StrictStr
    NodeConfiguration: ManagedBlockchainNodeConfiguration
    MemberId: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
