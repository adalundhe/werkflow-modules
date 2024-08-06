from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, StrictStr


class BackgroundColorMarkAttrs(BaseModel):
    color: StrictStr


class LinkMarkAttrs(BaseModel):
    collection: StrictStr | None = None
    href: StrictStr
    title: StrictStr | None = None
    id: StrictStr | None = None
    occurrenceKey: StrictStr | None = None


class SubSupMarkAttrs(BaseModel):
    type: Literal["sup", "sub"]


class TextColorAttrs(BaseModel):
    color: StrictStr
