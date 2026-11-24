from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .transcribe_media import TranscribeMedia
from .transcribe_medical_transcript import TranscribeMedicalTranscript
from .transcribe_medical_transcription_setting import TranscribeMedicalTranscriptionSetting
from .transcribe_tag import TranscribeTag


class TranscribeMedicalTranscriptionJob(BaseModel):
    MedicalTranscriptionJobName: StrictStr | None = None
    TranscriptionJobStatus: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    MediaSampleRateHertz: StrictInt | None = None
    MediaFormat: StrictStr | None = None
    Media: TranscribeMedia | None = None
    Transcript: TranscribeMedicalTranscript | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    Settings: TranscribeMedicalTranscriptionSetting | None = None
    ContentIdentificationType: StrictStr | None = None
    Specialty: StrictStr | None = None
    Type: StrictStr | None = None
    Tags: list[TranscribeTag] | None = None
