from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .transcribe_content_redaction import TranscribeContentRedaction
from .transcribe_job_execution_settings import TranscribeJobExecutionSettings
from .transcribe_language_id_settings import TranscribeLanguageIdSettings
from .transcribe_media import TranscribeMedia
from .transcribe_model_settings import TranscribeModelSettings
from .transcribe_settings import TranscribeSettings
from .transcribe_subtitles import TranscribeSubtitles
from .transcribe_tag import TranscribeTag
from .transcribe_toxicity_detection_settings import TranscribeToxicityDetectionSettings


class TranscribeStartTranscriptionJobRequest(BaseModel):
    TranscriptionJobName: StrictStr
    Media: TranscribeMedia
    LanguageCode: StrictStr | None = None
    MediaSampleRateHertz: StrictInt | None = None
    MediaFormat: Literal['mp3', 'mp4', 'wav', 'flac', 'ogg', 'amr', 'webm', 'm4a'] | None = None
    OutputBucketName: StrictStr | None = None
    OutputKey: StrictStr | None = None
    OutputEncryptionKMSKeyId: StrictStr | None = None
    KMSEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Settings: TranscribeSettings | None = None
    ModelSettings: TranscribeModelSettings | None = None
    JobExecutionSettings: TranscribeJobExecutionSettings | None = None
    ContentRedaction: TranscribeContentRedaction | None = None
    IdentifyLanguage: StrictBool | None = None
    IdentifyMultipleLanguages: StrictBool | None = None
    LanguageOptions: list[StrictStr] | None = None
    Subtitles: TranscribeSubtitles | None = None
    Tags: list[TranscribeTag] | None = None
    LanguageIdSettings: dict[StrictStr, TranscribeLanguageIdSettings] | None = None
    ToxicityDetection: list[TranscribeToxicityDetectionSettings] | None = None
