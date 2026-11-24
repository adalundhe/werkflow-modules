from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_ops_item_data_value import SSMOpsItemDataValue
from .ssm_ops_item_notification import SSMOpsItemNotification
from .ssm_related_ops_item import SSMRelatedOpsItem
from .ssm_tag import SSMTag


class SSMCreateOpsItemRequest(BaseModel):
    Description: StrictStr
    Source: StrictStr
    Title: StrictStr
    OpsItemType: StrictStr | None = None
    OperationalData: dict[StrictStr, SSMOpsItemDataValue] | None = None
    Notifications: list[SSMOpsItemNotification] | None = None
    Priority: StrictInt | None = None
    RelatedOpsItems: list[SSMRelatedOpsItem] | None = None
    Tags: list[SSMTag] | None = None
    Category: StrictStr | None = None
    Severity: StrictStr | None = None
    ActualStartTime: datetime.datetime | StrictStr | None = None
    ActualEndTime: datetime.datetime | StrictStr | None = None
    PlannedStartTime: datetime.datetime | StrictStr | None = None
    PlannedEndTime: datetime.datetime | StrictStr | None = None
    AccountId: StrictStr | None = None
