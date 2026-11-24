from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .comprehend_mention_sentiment import ComprehendMentionSentiment


class ComprehendTargetedSentimentMention(BaseModel):
    Score: StrictFloat | StrictInt | None = None
    GroupScore: StrictFloat | StrictInt | None = None
    Text: StrictStr | None = None
    Type: StrictStr | None = None
    MentionSentiment: ComprehendMentionSentiment | None = None
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
