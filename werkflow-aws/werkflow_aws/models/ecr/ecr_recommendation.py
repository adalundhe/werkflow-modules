from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRRecommendation(BaseModel):
    url: StrictStr | None = None
    text: StrictStr | None = None
