from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .q_business_attribute_filter import QBusinessAttributeFilter
from .q_business_chat_mode_configuration import QBusinessChatModeConfiguration


class QBusinessConfigurationEvent(BaseModel):
    chatMode: Literal['RETRIEVAL_MODE', 'CREATOR_MODE', 'PLUGIN_MODE'] | None = None
    chatModeConfiguration: QBusinessChatModeConfiguration | None = None
    attributeFilter: QBusinessAttributeFilter | None = None
