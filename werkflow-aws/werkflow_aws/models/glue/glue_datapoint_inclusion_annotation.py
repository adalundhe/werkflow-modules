from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GlueDatapointInclusionAnnotation(BaseModel):
    ProfileId: StrictStr | None = None
    StatisticId: StrictStr | None = None
    InclusionAnnotation: Literal['INCLUDE', 'EXCLUDE'] | None = None
