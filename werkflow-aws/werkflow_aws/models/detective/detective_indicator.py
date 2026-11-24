from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .detective_indicator_detail import DetectiveIndicatorDetail


class DetectiveIndicator(BaseModel):
    IndicatorType: StrictStr | None = None
    IndicatorDetail: DetectiveIndicatorDetail | None = None
