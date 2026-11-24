from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_item_data_value import SSMOpsItemDataValue
from .ssm_ops_item_notification import SSMOpsItemNotification
from .ssm_related_ops_item import SSMRelatedOpsItem


class SSMUpdateOpsItemRequest(BaseModel):
    OpsItemId: StrictStr
    Description: StrictStr | None = None
    OperationalData: dict[StrictStr, SSMOpsItemDataValue] | None = None
    OperationalDataToDelete: list[StrictStr] | None = None
    Notifications: list[SSMOpsItemNotification] | None = None
    Priority: StrictInt | None = None
    RelatedOpsItems: list[SSMRelatedOpsItem] | None = None
    Status: Literal['Open', 'InProgress', 'Resolved', 'Pending', 'TimedOut', 'Cancelling', 'Cancelled', 'Failed', 'CompletedWithSuccess', 'CompletedWithFailure', 'Scheduled', 'RunbookInProgress', 'PendingChangeCalendarOverride', 'ChangeCalendarOverrideApproved', 'ChangeCalendarOverrideRejected', 'PendingApproval', 'Approved', 'Revoked', 'Rejected', 'Closed'] | None = None
    Title: StrictStr | None = None
    Category: StrictStr | None = None
    Severity: StrictStr | None = None
    ActualStartTime: datetime.datetime | StrictStr | None = None
    ActualEndTime: datetime.datetime | StrictStr | None = None
    PlannedStartTime: datetime.datetime | StrictStr | None = None
    PlannedEndTime: datetime.datetime | StrictStr | None = None
    OpsItemArn: StrictStr | None = None
