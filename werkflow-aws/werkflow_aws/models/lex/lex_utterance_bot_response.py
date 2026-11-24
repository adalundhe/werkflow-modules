from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_image_response_card import LexImageResponseCard


class LexUtteranceBotResponse(BaseModel):
    content: StrictStr | None = None
    contentType: StrictStr | None = None
    imageResponseCard: LexImageResponseCard | None = None
