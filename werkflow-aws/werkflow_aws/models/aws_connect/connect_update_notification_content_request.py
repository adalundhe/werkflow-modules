from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectUpdateNotificationContentRequest(BaseModel):
    InstanceId: StrictStr
    NotificationId: StrictStr
    Content: dict[Literal['en_US', 'de_DE', 'es_ES', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'zh_CN', 'zh_TW'], StrictStr]
