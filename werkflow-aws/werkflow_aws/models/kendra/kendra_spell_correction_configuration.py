from __future__ import annotations
from pydantic import BaseModel, StrictBool


class KendraSpellCorrectionConfiguration(BaseModel):
    IncludeQuerySpellCheckSuggestions: StrictBool
