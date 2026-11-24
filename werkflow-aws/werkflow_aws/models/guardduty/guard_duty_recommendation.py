from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyRecommendation(BaseModel):
    Title: StrictStr | None = None
    Rationale: StrictStr | None = None
    Category: StrictStr | None = None
    Priority: StrictStr | None = None
    CliCommands: list[StrictStr] | None = None
