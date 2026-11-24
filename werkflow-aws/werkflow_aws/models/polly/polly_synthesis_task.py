from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class PollySynthesisTask(BaseModel):
    Engine: StrictStr | None = None
    TaskId: StrictStr | None = None
    TaskStatus: StrictStr | None = None
    TaskStatusReason: StrictStr | None = None
    OutputUri: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    RequestCharacters: StrictInt | None = None
    SnsTopicArn: StrictStr | None = None
    LexiconNames: list[StrictStr] | None = None
    OutputFormat: StrictStr | None = None
    SampleRate: StrictStr | None = None
    SpeechMarkTypes: list[StrictStr] | None = None
    TextType: StrictStr | None = None
    VoiceId: StrictStr | None = None
    LanguageCode: StrictStr | None = None
