from __future__ import annotations
from pydantic import BaseModel
from .lex_conversation_logs_data_source import LexConversationLogsDataSource


class LexTestSetGenerationDataSource(BaseModel):
    conversationLogsDataSource: LexConversationLogsDataSource | None = None
