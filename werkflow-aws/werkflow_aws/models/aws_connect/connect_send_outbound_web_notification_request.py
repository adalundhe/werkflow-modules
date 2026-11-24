from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_web_notification_content import ConnectWebNotificationContent
from .connect_web_notification_source import ConnectWebNotificationSource
from .connect_widget_destination import ConnectWidgetDestination


class ConnectSendOutboundWebNotificationRequest(BaseModel):
    InstanceId: StrictStr
    BrowserId: StrictStr
    SessionId: StrictStr
    ExpiresAt: datetime.datetime | StrictStr
    Source: ConnectWebNotificationSource
    Destination: ConnectWidgetDestination
    Content: ConnectWebNotificationContent
    ClientToken: StrictStr | None = None
