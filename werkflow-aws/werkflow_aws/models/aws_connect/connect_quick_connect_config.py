from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_flow_quick_connect_config import ConnectFlowQuickConnectConfig
from .connect_phone_number_quick_connect_config import ConnectPhoneNumberQuickConnectConfig
from .connect_queue_quick_connect_config import ConnectQueueQuickConnectConfig
from .connect_user_quick_connect_config import ConnectUserQuickConnectConfig


class ConnectQuickConnectConfig(BaseModel):
    QuickConnectType: StrictStr | None = None
    UserConfig: ConnectUserQuickConnectConfig | None = None
    QueueConfig: ConnectQueueQuickConnectConfig | None = None
    PhoneConfig: ConnectPhoneNumberQuickConnectConfig | None = None
    FlowConfig: ConnectFlowQuickConnectConfig | None = None
