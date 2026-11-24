from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_alias_history_event import LexBotAliasHistoryEvent
from .lex_bot_alias_locale_settings import LexBotAliasLocaleSettings
from .lex_conversation_log_settings import LexConversationLogSettings
from .lex_parent_bot_network import LexParentBotNetwork
from .lex_sentiment_analysis_settings import LexSentimentAnalysisSettings


class LexDescribeBotAliasResponse(BaseModel):
    botAliasId: StrictStr | None = None
    botAliasName: StrictStr | None = None
    description: StrictStr | None = None
    botVersion: StrictStr | None = None
    botAliasLocaleSettings: dict[StrictStr, LexBotAliasLocaleSettings] | None = None
    conversationLogSettings: LexConversationLogSettings | None = None
    sentimentAnalysisSettings: LexSentimentAnalysisSettings | None = None
    botAliasHistoryEvents: list[LexBotAliasHistoryEvent] | None = None
    botAliasStatus: StrictStr | None = None
    botId: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    parentBotNetworks: list[LexParentBotNetwork] | None = None
    ResponseMetadata: dict[str, Any] | None = None
