from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .transcribe_media import TranscribeMedia
from .transcribe_medical_transcription_setting import TranscribeMedicalTranscriptionSetting
from .transcribe_tag import TranscribeTag


class TranscribeStartMedicalTranscriptionJobRequest(BaseModel):
    MedicalTranscriptionJobName: StrictStr
    LanguageCode: StrictStr
    Media: TranscribeMedia
    OutputBucketName: StrictStr
    Specialty: Literal['PRIMARYCARE']
    Type: Literal['CONVERSATION', 'DICTATION']
    MediaSampleRateHertz: StrictInt | None = None
    MediaFormat: Literal['mp3', 'mp4', 'wav', 'flac', 'ogg', 'amr', 'webm', 'm4a'] | None = None
    OutputKey: StrictStr | None = None
    OutputEncryptionKMSKeyId: StrictStr | None = None
    KMSEncryptionContext: dict[StrictStr, StrictStr] | None = None
    Settings: TranscribeMedicalTranscriptionSetting | None = None
    ContentIdentificationType: Literal['PHI'] | None = None
    Tags: list[TranscribeTag] | None = None
