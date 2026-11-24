from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_placement_statistics import SESPlacementStatistics


class SESIspPlacement(BaseModel):
    IspName: StrictStr | None = None
    PlacementStatistics: SESPlacementStatistics | None = None
