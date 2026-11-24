from __future__ import annotations
from pydantic import BaseModel
from .msk_replicator_log_delivery import MSKReplicatorLogDelivery


class MSKLogDelivery(BaseModel):
    ReplicatorLogDelivery: MSKReplicatorLogDelivery | None = None
