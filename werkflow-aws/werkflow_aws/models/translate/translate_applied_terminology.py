from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .translate_term import TranslateTerm


class TranslateAppliedTerminology(BaseModel):
    Name: StrictStr | None = None
    Terms: list[TranslateTerm] | None = None
