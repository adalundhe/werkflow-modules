from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_after_contact_work_config_per_channel import ConnectAfterContactWorkConfigPerChannel
from .connect_auto_accept_config import ConnectAutoAcceptConfig
from .connect_persistent_connection_config import ConnectPersistentConnectionConfig
from .connect_phone_number_config import ConnectPhoneNumberConfig
from .connect_user_identity_info_lite import ConnectUserIdentityInfoLite
from .connect_user_phone_config import ConnectUserPhoneConfig
from .connect_voice_enhancement_config import ConnectVoiceEnhancementConfig


class ConnectUserSearchSummary(BaseModel):
    Arn: StrictStr | None = None
    DirectoryUserId: StrictStr | None = None
    HierarchyGroupId: StrictStr | None = None
    Id: StrictStr | None = None
    IdentityInfo: ConnectUserIdentityInfoLite | None = None
    PhoneConfig: ConnectUserPhoneConfig | None = None
    RoutingProfileId: StrictStr | None = None
    SecurityProfileIds: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    Username: StrictStr | None = None
    AutoAcceptConfigs: list[ConnectAutoAcceptConfig] | None = None
    AfterContactWorkConfigs: list[ConnectAfterContactWorkConfigPerChannel] | None = None
    PhoneNumberConfigs: list[ConnectPhoneNumberConfig] | None = None
    PersistentConnectionConfigs: list[ConnectPersistentConnectionConfig] | None = None
    VoiceEnhancementConfigs: list[ConnectVoiceEnhancementConfig] | None = None
