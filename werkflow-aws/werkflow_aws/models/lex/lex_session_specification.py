from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_invoked_intent_sample import LexInvokedIntentSample


class LexSessionSpecification(BaseModel):
    botAliasId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    channel: StrictStr | None = None
    sessionId: StrictStr | None = None
    conversationStartTime: datetime.datetime | StrictStr | None = None
    conversationEndTime: datetime.datetime | StrictStr | None = None
    conversationDurationSeconds: StrictInt | None = None
    conversationEndState: StrictStr | None = None
    mode: StrictStr | None = None
    numberOfTurns: StrictInt | None = None
    invokedIntentSamples: list[LexInvokedIntentSample] | None = None
    originatingRequestId: StrictStr | None = None
