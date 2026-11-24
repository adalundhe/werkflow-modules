from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .transcribe_call_analytics_job_details import TranscribeCallAnalyticsJobDetails
from .transcribe_call_analytics_job_settings import TranscribeCallAnalyticsJobSettings
from .transcribe_channel_definition import TranscribeChannelDefinition
from .transcribe_media import TranscribeMedia
from .transcribe_tag import TranscribeTag
from .transcribe_transcript import TranscribeTranscript


class TranscribeCallAnalyticsJob(BaseModel):
    CallAnalyticsJobName: StrictStr | None = None
    CallAnalyticsJobStatus: StrictStr | None = None
    CallAnalyticsJobDetails: TranscribeCallAnalyticsJobDetails | None = None
    LanguageCode: StrictStr | None = None
    MediaSampleRateHertz: StrictInt | None = None
    MediaFormat: StrictStr | None = None
    Media: TranscribeMedia | None = None
    Transcript: TranscribeTranscript | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    CompletionTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    DataAccessRoleArn: StrictStr | None = None
    IdentifiedLanguageScore: StrictFloat | StrictInt | None = None
    Settings: TranscribeCallAnalyticsJobSettings | None = None
    ChannelDefinitions: list[TranscribeChannelDefinition] | None = None
    Tags: list[TranscribeTag] | None = None
