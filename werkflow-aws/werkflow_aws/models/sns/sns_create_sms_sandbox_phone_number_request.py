from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SNSCreateSMSSandboxPhoneNumberRequest(BaseModel):
    PhoneNumber: StrictStr
    LanguageCode: Literal['en-US', 'en-GB', 'es-419', 'es-ES', 'de-DE', 'fr-CA', 'fr-FR', 'it-IT', 'ja-JP', 'pt-BR', 'kr-KR', 'zh-CN', 'zh-TW'] | None = None
