from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_encryption_setting import LexEncryptionSetting
from .lex_transcript_source_setting import LexTranscriptSourceSetting


class LexUpdateBotRecommendationResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    botRecommendationStatus: StrictStr | None = None
    botRecommendationId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    transcriptSourceSetting: LexTranscriptSourceSetting | None = None
    encryptionSetting: LexEncryptionSetting | None = None
    ResponseMetadata: dict[str, Any] | None = None
