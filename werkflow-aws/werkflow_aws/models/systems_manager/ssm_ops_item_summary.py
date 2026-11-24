from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_item_data_value import SSMOpsItemDataValue


class SSMOpsItemSummary(BaseModel):
    CreatedBy: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastModifiedBy: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    Priority: StrictInt | None = None
    Source: StrictStr | None = None
    Status: StrictStr | None = None
    OpsItemId: StrictStr | None = None
    Title: StrictStr | None = None
    OperationalData: dict[StrictStr, SSMOpsItemDataValue] | None = None
    Category: StrictStr | None = None
    Severity: StrictStr | None = None
    OpsItemType: StrictStr | None = None
    ActualStartTime: datetime.datetime | StrictStr | None = None
    ActualEndTime: datetime.datetime | StrictStr | None = None
    PlannedStartTime: datetime.datetime | StrictStr | None = None
    PlannedEndTime: datetime.datetime | StrictStr | None = None
