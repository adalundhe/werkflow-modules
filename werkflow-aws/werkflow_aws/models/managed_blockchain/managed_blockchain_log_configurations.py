from __future__ import annotations
from pydantic import BaseModel
from .managed_blockchain_log_configuration import ManagedBlockchainLogConfiguration


class ManagedBlockchainLogConfigurations(BaseModel):
    Cloudwatch: ManagedBlockchainLogConfiguration | None = None
