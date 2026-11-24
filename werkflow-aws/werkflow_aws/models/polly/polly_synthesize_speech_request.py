from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class PollySynthesizeSpeechRequest(BaseModel):
    OutputFormat: Literal['json', 'mp3', 'ogg_opus', 'ogg_vorbis', 'pcm', 'mulaw', 'alaw']
    Text: StrictStr
    VoiceId: StrictStr
    Engine: Literal['standard', 'neural', 'long-form', 'generative'] | None = None
    LanguageCode: StrictStr | None = None
    LexiconNames: list[StrictStr] | None = None
    SampleRate: StrictStr | None = None
    SpeechMarkTypes: list[Literal['sentence', 'ssml', 'viseme', 'word']] | None = None
    TextType: Literal['ssml', 'text'] | None = None
