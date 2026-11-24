from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractFigureCaptionConfiguration(BaseModel):
    State: StrictStr | None = None
