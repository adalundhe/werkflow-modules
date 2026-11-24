from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_inventory_deletion_status_item import SSMInventoryDeletionStatusItem


class SSMDescribeInventoryDeletionsResponse(BaseModel):
    InventoryDeletions: list[SSMInventoryDeletionStatusItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
