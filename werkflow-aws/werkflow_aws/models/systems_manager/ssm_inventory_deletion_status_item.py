from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_inventory_deletion_summary import SSMInventoryDeletionSummary


class SSMInventoryDeletionStatusItem(BaseModel):
    DeletionId: StrictStr | None = None
    TypeName: StrictStr | None = None
    DeletionStartTime: datetime.datetime | StrictStr | None = None
    LastStatus: StrictStr | None = None
    LastStatusMessage: StrictStr | None = None
    DeletionSummary: SSMInventoryDeletionSummary | None = None
    LastStatusUpdateTime: datetime.datetime | StrictStr | None = None
