from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_notification_search_criteria import ConnectNotificationSearchCriteria
from .connect_notification_search_filter import ConnectNotificationSearchFilter


class ConnectSearchNotificationsRequest(BaseModel):
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    SearchFilter: ConnectNotificationSearchFilter | None = None
    SearchCriteria: ConnectNotificationSearchCriteria | None = None
