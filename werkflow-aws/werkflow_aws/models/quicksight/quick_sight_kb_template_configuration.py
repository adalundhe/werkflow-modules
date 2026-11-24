from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_kb_template import QuickSightKbTemplate


class QuickSightKbTemplateConfiguration(BaseModel):
    template: QuickSightKbTemplate | None = None
