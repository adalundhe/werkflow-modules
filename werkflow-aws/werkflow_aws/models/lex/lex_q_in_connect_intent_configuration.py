from __future__ import annotations
from pydantic import BaseModel
from .lex_q_in_connect_assistant_configuration import LexQInConnectAssistantConfiguration


class LexQInConnectIntentConfiguration(BaseModel):
    qInConnectAssistantConfiguration: LexQInConnectAssistantConfiguration | None = None
