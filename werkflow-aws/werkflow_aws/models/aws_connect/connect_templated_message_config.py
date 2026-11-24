from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_template_attributes import ConnectTemplateAttributes


class ConnectTemplatedMessageConfig(BaseModel):
    KnowledgeBaseId: StrictStr
    MessageTemplateId: StrictStr
    TemplateAttributes: ConnectTemplateAttributes
