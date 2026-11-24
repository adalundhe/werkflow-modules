from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lex_utterance_bot_response import LexUtteranceBotResponse


class LexUtteranceSpecification(BaseModel):
    botAliasId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    sessionId: StrictStr | None = None
    channel: StrictStr | None = None
    mode: StrictStr | None = None
    conversationStartTime: datetime.datetime | StrictStr | None = None
    conversationEndTime: datetime.datetime | StrictStr | None = None
    utterance: StrictStr | None = None
    utteranceTimestamp: datetime.datetime | StrictStr | None = None
    audioVoiceDurationMillis: StrictInt | None = None
    utteranceUnderstood: StrictBool | None = None
    inputType: StrictStr | None = None
    outputType: StrictStr | None = None
    associatedIntentName: StrictStr | None = None
    associatedSlotName: StrictStr | None = None
    intentState: StrictStr | None = None
    dialogActionType: StrictStr | None = None
    botResponseAudioVoiceId: StrictStr | None = None
    slotsFilledInSession: StrictStr | None = None
    utteranceRequestId: StrictStr | None = None
    botResponses: list[LexUtteranceBotResponse] | None = None
