from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .transcribe_media import TranscribeMedia
from .transcribe_medical_scribe_channel_definition import TranscribeMedicalScribeChannelDefinition
from .transcribe_medical_scribe_output import TranscribeMedicalScribeOutput
from .transcribe_medical_scribe_settings import TranscribeMedicalScribeSettings
from .transcribe_tag import TranscribeTag


class TranscribeMedicalScribeJob(BaseModel):
    MedicalScribeJobName: StrictStr | None = None
    MedicalScribeJobStatus: StrictStr | None = None
    LanguageCode: StrictStr | None = None
    Media: TranscribeMedia | None = None
    MedicalScribeOutput: TranscribeMedicalScribeOutput | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    Settings: TranscribeMedicalScribeSettings | None = None
    DataAccessRoleArn: StrictStr | None = None
    ChannelDefinitions: list[TranscribeMedicalScribeChannelDefinition] | None = None
    MedicalScribeContextProvided: StrictBool | None = None
    Tags: list[TranscribeTag] | None = None
