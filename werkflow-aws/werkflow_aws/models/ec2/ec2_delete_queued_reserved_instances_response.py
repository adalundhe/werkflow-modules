from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_failed_queued_purchase_deletion import EC2FailedQueuedPurchaseDeletion
from .ec2_successful_queued_purchase_deletion import EC2SuccessfulQueuedPurchaseDeletion


class EC2DeleteQueuedReservedInstancesResponse(BaseModel):
    SuccessfulQueuedPurchaseDeletions: list[EC2SuccessfulQueuedPurchaseDeletion] | None = None
    FailedQueuedPurchaseDeletions: list[EC2FailedQueuedPurchaseDeletion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
