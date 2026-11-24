from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_context_menu_option import QuickSightContextMenuOption
from .quick_sight_visual_menu_option import QuickSightVisualMenuOption


class QuickSightVisualInteractionOptions(BaseModel):
    VisualMenuOption: QuickSightVisualMenuOption | None = None
    ContextMenuOption: QuickSightContextMenuOption | None = None
