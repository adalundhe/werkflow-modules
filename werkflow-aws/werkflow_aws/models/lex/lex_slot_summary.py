from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lex_prompt_specification import LexPromptSpecification


class LexSlotSummary(BaseModel):
    slotId: StrictStr | None = None
    slotName: StrictStr | None = None
    description: StrictStr | None = None
    slotConstraint: StrictStr | None = None
    slotTypeId: StrictStr | None = None
    valueElicitationPromptSpecification: LexPromptSpecification | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
