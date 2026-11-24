from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .transcribe_content_redaction import TranscribeContentRedaction
from .transcribe_language_code_item import TranscribeLanguageCodeItem
from .transcribe_model_settings import TranscribeModelSettings
from .transcribe_toxicity_detection_settings import TranscribeToxicityDetectionSettings


class TranscribeTranscriptionJobSummary(BaseModel):
    TranscriptionJobName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    LanguageCode: StrictStr | None = None
    TranscriptionJobStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    OutputLocationType: StrictStr | None = None
    ContentRedaction: TranscribeContentRedaction | None = None
    ModelSettings: TranscribeModelSettings | None = None
    IdentifyLanguage: StrictBool | None = None
    IdentifyMultipleLanguages: StrictBool | None = None
    IdentifiedLanguageScore: StrictFloat | StrictInt | None = None
    LanguageCodes: list[TranscribeLanguageCodeItem] | None = None
    ToxicityDetection: list[TranscribeToxicityDetectionSettings] | None = None
