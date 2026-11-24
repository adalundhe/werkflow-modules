from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .managed_blockchain_node_log_publishing_configuration import ManagedBlockchainNodeLogPublishingConfiguration


class ManagedBlockchainNodeConfiguration(BaseModel):
    InstanceType: StrictStr
    AvailabilityZone: StrictStr | None = None
    LogPublishingConfiguration: ManagedBlockchainNodeLogPublishingConfiguration | None = None
    StateDB: Literal['LevelDB', 'CouchDB'] | None = None
