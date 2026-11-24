from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_visual_message_configuration import QuickSightVisualMessageConfiguration


class QuickSightVisualMessages(BaseModel):
    NoDataMessage: QuickSightVisualMessageConfiguration | None = None
