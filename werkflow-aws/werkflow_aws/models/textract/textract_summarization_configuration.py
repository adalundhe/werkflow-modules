from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractSummarizationConfiguration(BaseModel):
    State: StrictStr | None = None
