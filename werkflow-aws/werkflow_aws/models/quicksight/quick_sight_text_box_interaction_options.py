from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_text_box_menu_option import QuickSightTextBoxMenuOption


class QuickSightTextBoxInteractionOptions(BaseModel):
    TextBoxMenuOption: QuickSightTextBoxMenuOption | None = None
