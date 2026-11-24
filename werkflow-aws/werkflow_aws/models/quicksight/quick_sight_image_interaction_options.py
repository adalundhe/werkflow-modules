from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_image_menu_option import QuickSightImageMenuOption


class QuickSightImageInteractionOptions(BaseModel):
    ImageMenuOption: QuickSightImageMenuOption | None = None
