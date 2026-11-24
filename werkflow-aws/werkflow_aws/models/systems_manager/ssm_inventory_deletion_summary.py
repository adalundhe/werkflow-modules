from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ssm_inventory_deletion_summary_item import SSMInventoryDeletionSummaryItem


class SSMInventoryDeletionSummary(BaseModel):
    TotalCount: StrictInt | None = None
    RemainingCount: StrictInt | None = None
    SummaryItems: list[SSMInventoryDeletionSummaryItem] | None = None
