from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_kb_template_configuration import QuickSightKbTemplateConfiguration


class QuickSightKnowledgeBaseConfiguration(BaseModel):
    templateConfiguration: QuickSightKbTemplateConfiguration | None = None
