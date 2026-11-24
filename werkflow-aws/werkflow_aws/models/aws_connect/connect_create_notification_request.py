from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectCreateNotificationRequest(BaseModel):
    InstanceId: StrictStr
    Recipients: list[StrictStr]
    Content: dict[Literal['en_US', 'de_DE', 'es_ES', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'zh_CN', 'zh_TW'], StrictStr]
    ExpiresAt: datetime.datetime | StrictStr | None = None
    Priority: Literal['HIGH', 'LOW'] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    PredefinedNotificationId: StrictStr | None = None
    ClientToken: StrictStr | None = None
