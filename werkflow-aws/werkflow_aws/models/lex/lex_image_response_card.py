from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_button import LexButton


class LexImageResponseCard(BaseModel):
    title: StrictStr | None = None
    subtitle: StrictStr | None = None
    imageUrl: StrictStr | None = None
    buttons: list[LexButton] | None = None
