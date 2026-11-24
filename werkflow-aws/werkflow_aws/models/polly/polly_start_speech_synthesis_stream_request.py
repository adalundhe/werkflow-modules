from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .polly_start_speech_synthesis_stream_action_stream import PollyStartSpeechSynthesisStreamActionStream


class PollyStartSpeechSynthesisStreamRequest(BaseModel):
    Engine: Literal['standard', 'neural', 'long-form', 'generative']
    OutputFormat: Literal['json', 'mp3', 'ogg_opus', 'ogg_vorbis', 'pcm', 'mulaw', 'alaw']
    VoiceId: StrictStr
    LanguageCode: StrictStr | None = None
    LexiconNames: list[StrictStr] | None = None
    SampleRate: StrictStr | None = None
    ActionStream: PollyStartSpeechSynthesisStreamActionStream | None = None
