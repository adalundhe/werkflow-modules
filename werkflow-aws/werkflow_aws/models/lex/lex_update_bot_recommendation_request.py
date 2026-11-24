from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_encryption_setting import LexEncryptionSetting


class LexUpdateBotRecommendationRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    botRecommendationId: StrictStr
    encryptionSetting: LexEncryptionSetting
