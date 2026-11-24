from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexExactResponseFields(BaseModel):
    questionField: StrictStr | None = None
    answerField: StrictStr | None = None
