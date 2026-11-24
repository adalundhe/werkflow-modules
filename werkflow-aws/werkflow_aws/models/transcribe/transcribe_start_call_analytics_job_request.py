from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transcribe_call_analytics_job_settings import TranscribeCallAnalyticsJobSettings
from .transcribe_channel_definition import TranscribeChannelDefinition
from .transcribe_media import TranscribeMedia
from .transcribe_tag import TranscribeTag


class TranscribeStartCallAnalyticsJobRequest(BaseModel):
    CallAnalyticsJobName: StrictStr
    Media: TranscribeMedia
    OutputLocation: StrictStr | None = None
    OutputEncryptionKMSKeyId: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    Settings: TranscribeCallAnalyticsJobSettings | None = None
    Tags: list[TranscribeTag] | None = None
    ChannelDefinitions: list[TranscribeChannelDefinition] | None = None
