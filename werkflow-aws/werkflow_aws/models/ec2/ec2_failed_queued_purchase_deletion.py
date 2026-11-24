from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_delete_queued_reserved_instances_error import EC2DeleteQueuedReservedInstancesError


class EC2FailedQueuedPurchaseDeletion(BaseModel):
    Error: EC2DeleteQueuedReservedInstancesError | None = None
    ReservedInstancesId: StrictStr | None = None
