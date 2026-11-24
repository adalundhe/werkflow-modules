from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .transcribe_content_redaction import TranscribeContentRedaction
from .transcribe_job_execution_settings import TranscribeJobExecutionSettings
from .transcribe_language_code_item import TranscribeLanguageCodeItem
from .transcribe_language_id_settings import TranscribeLanguageIdSettings
from .transcribe_media import TranscribeMedia
from .transcribe_model_settings import TranscribeModelSettings
from .transcribe_settings import TranscribeSettings
from .transcribe_subtitles_output import TranscribeSubtitlesOutput
from .transcribe_tag import TranscribeTag
from .transcribe_toxicity_detection_settings import TranscribeToxicityDetectionSettings
from .transcribe_transcript import TranscribeTranscript


class TranscribeTranscriptionJob(BaseModel):
    TranscriptionJobName: StrictStr | None = None
    TranscriptionJobStatus: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    MediaSampleRateHertz: StrictInt | None = None
    MediaFormat: StrictStr | None = None
    Media: TranscribeMedia | None = None
    Transcript: TranscribeTranscript | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    Settings: TranscribeSettings | None = None
    ModelSettings: TranscribeModelSettings | None = None
    JobExecutionSettings: TranscribeJobExecutionSettings | None = None
    ContentRedaction: TranscribeContentRedaction | None = None
    IdentifyLanguage: StrictBool | None = None
    IdentifyMultipleLanguages: StrictBool | None = None
    LanguageOptions: list[StrictStr] | None = None
    IdentifiedLanguageScore: StrictFloat | StrictInt | None = None
    LanguageCodes: list[TranscribeLanguageCodeItem] | None = None
    Tags: list[TranscribeTag] | None = None
    Subtitles: TranscribeSubtitlesOutput | None = None
    LanguageIdSettings: dict[StrictStr, TranscribeLanguageIdSettings] | None = None
    ToxicityDetection: list[TranscribeToxicityDetectionSettings] | None = None
