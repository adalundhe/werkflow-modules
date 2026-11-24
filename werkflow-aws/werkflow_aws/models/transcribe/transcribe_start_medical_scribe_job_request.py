from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_media import TranscribeMedia
from .transcribe_medical_scribe_channel_definition import TranscribeMedicalScribeChannelDefinition
from .transcribe_medical_scribe_context import TranscribeMedicalScribeContext
from .transcribe_medical_scribe_settings import TranscribeMedicalScribeSettings
from .transcribe_tag import TranscribeTag


class TranscribeStartMedicalScribeJobRequest(BaseModel):
    MedicalScribeJobName: StrictStr
    Media: TranscribeMedia
    OutputBucketName: StrictStr
    DataAccessRoleArn: StrictStr
    Settings: TranscribeMedicalScribeSettings
    OutputEncryptionKMSKeyId: StrictStr | None = None
    KMSEncryptionContext: dict[StrictStr, StrictStr] | None = None
    ChannelDefinitions: list[TranscribeMedicalScribeChannelDefinition] | None = None
    Tags: list[TranscribeTag] | None = None
    MedicalScribeContext: TranscribeMedicalScribeContext | None = None
