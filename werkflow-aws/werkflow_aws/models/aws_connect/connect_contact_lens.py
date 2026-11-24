from __future__ import annotations
from pydantic import BaseModel
from .connect_conversational_analytics import ConnectConversationalAnalytics


class ConnectContactLens(BaseModel):
    ConversationalAnalytics: ConnectConversationalAnalytics | None = None
