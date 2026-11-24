from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_content_redaction import TranscribeContentRedaction
from .transcribe_language_id_settings import TranscribeLanguageIdSettings
from .transcribe_summarization import TranscribeSummarization


class TranscribeCallAnalyticsJobSettings(BaseModel):
    VocabularyName: StrictStr | None = None
    VocabularyFilterName: StrictStr | None = None
    VocabularyFilterMethod: StrictStr | None = None
    LanguageModelName: StrictStr | None = None
    ContentRedaction: TranscribeContentRedaction | None = None
    LanguageOptions: list[StrictStr] | None = None
    LanguageIdSettings: dict[StrictStr, TranscribeLanguageIdSettings] | None = None
    Summarization: TranscribeSummarization | None = None
