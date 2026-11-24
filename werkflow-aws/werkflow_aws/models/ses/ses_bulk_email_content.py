from __future__ import annotations
from pydantic import BaseModel
from .ses_template import SESTemplate


class SESBulkEmailContent(BaseModel):
    Template: SESTemplate | None = None
