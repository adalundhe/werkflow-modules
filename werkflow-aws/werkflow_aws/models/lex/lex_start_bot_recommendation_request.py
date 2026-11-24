from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_encryption_setting import LexEncryptionSetting
from .lex_transcript_source_setting import LexTranscriptSourceSetting


class LexStartBotRecommendationRequest(BaseModel):
    botId: StrictStr
    botVersion: StrictStr
    localeId: StrictStr
    transcriptSourceSetting: LexTranscriptSourceSetting
    encryptionSetting: LexEncryptionSetting | None = None
