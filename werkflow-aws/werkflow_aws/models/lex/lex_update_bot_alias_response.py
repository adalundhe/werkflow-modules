from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_alias_locale_settings import LexBotAliasLocaleSettings
from .lex_conversation_log_settings import LexConversationLogSettings
from .lex_sentiment_analysis_settings import LexSentimentAnalysisSettings


class LexUpdateBotAliasResponse(BaseModel):
    botAliasId: StrictStr | None = None
    botAliasName: StrictStr | None = None
    description: StrictStr | None = None
    botVersion: StrictStr | None = None
    botAliasLocaleSettings: dict[StrictStr, LexBotAliasLocaleSettings] | None = None
    conversationLogSettings: LexConversationLogSettings | None = None
    sentimentAnalysisSettings: LexSentimentAnalysisSettings | None = None
    botAliasStatus: StrictStr | None = None
    botId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
