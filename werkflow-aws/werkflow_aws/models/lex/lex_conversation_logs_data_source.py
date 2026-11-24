from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_conversation_logs_data_source_filter_by import LexConversationLogsDataSourceFilterBy


class LexConversationLogsDataSource(BaseModel):
    botId: StrictStr | None = None
    botAliasId: StrictStr | None = None
    localeId: StrictStr | None = None
    filter: LexConversationLogsDataSourceFilterBy | None = None
