from __future__ import annotations
from pydantic import BaseModel
from .lex_custom_payload import LexCustomPayload
from .lex_image_response_card import LexImageResponseCard
from .lex_plain_text_message import LexPlainTextMessage
from .lex_ssml_message import LexSSMLMessage


class LexMessage(BaseModel):
    plainTextMessage: LexPlainTextMessage | None = None
    customPayload: LexCustomPayload | None = None
    ssmlMessage: LexSSMLMessage | None = None
    imageResponseCard: LexImageResponseCard | None = None
