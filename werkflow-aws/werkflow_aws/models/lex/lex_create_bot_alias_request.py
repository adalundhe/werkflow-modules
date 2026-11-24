from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_bot_alias_locale_settings import LexBotAliasLocaleSettings
from .lex_conversation_log_settings import LexConversationLogSettings
from .lex_sentiment_analysis_settings import LexSentimentAnalysisSettings


class LexCreateBotAliasRequest(BaseModel):
    botAliasName: StrictStr
    botId: StrictStr
    description: StrictStr | None = None
    botVersion: StrictStr | None = None
    botAliasLocaleSettings: dict[StrictStr, LexBotAliasLocaleSettings] | None = None
    conversationLogSettings: LexConversationLogSettings | None = None
    sentimentAnalysisSettings: LexSentimentAnalysisSettings | None = None
    tags: dict[StrictStr, StrictStr] | None = None
