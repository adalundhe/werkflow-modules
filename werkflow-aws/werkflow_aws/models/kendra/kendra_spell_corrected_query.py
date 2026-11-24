from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_correction import KendraCorrection


class KendraSpellCorrectedQuery(BaseModel):
    SuggestedQueryText: StrictStr | None = None
    Corrections: list[KendraCorrection] | None = None
