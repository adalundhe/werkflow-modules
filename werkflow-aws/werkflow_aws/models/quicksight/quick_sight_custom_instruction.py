from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_inline_custom_instruction import QuickSightInlineCustomInstruction


class QuickSightCustomInstruction(BaseModel):
    InlineCustomInstruction: QuickSightInlineCustomInstruction | None = None
