from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class JiraRichTextInput(BaseModel):
    adfValue: dict[StrictStr, Any] | None = None
