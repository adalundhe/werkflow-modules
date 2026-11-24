from __future__ import annotations
from pydantic import BaseModel
from .ses_replacement_template import SESReplacementTemplate


class SESReplacementEmailContent(BaseModel):
    ReplacementTemplate: SESReplacementTemplate | None = None
