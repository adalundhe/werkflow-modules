from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, StrictStr


class EmojiAttrs(BaseModel):
    shortName: StrictStr
    text: StrictStr
    id: StrictStr


EmojirAttrs = EmojiAttrs


class InlineCardAttrs(BaseModel):
    url: StrictStr


class HardBreakAttrs(BaseModel):
    text: StrictStr


class MentionAttrs(BaseModel):
    id: StrictStr
    text: StrictStr
    userType: Literal["DEFAULT", "SPECIAL", "APP"] = "DEFAULT"
