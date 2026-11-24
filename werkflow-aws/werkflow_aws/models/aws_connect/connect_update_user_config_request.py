from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_after_contact_work_config_per_channel import ConnectAfterContactWorkConfigPerChannel
from .connect_auto_accept_config import ConnectAutoAcceptConfig
from .connect_persistent_connection_config import ConnectPersistentConnectionConfig
from .connect_phone_number_config import ConnectPhoneNumberConfig
from .connect_voice_enhancement_config import ConnectVoiceEnhancementConfig


class ConnectUpdateUserConfigRequest(BaseModel):
    UserId: StrictStr
    InstanceId: StrictStr
    AutoAcceptConfigs: list[ConnectAutoAcceptConfig] | None = None
    AfterContactWorkConfigs: list[ConnectAfterContactWorkConfigPerChannel] | None = None
    PhoneNumberConfigs: list[ConnectPhoneNumberConfig] | None = None
    PersistentConnectionConfigs: list[ConnectPersistentConnectionConfig] | None = None
    VoiceEnhancementConfigs: list[ConnectVoiceEnhancementConfig] | None = None
