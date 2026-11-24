from __future__ import annotations
from pydantic import BaseModel
from .ses_content import SESContent


class SESBody(BaseModel):
    Text: SESContent | None = None
    Html: SESContent | None = None
