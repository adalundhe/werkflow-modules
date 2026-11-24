from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GluePutDataQualityProfileAnnotationRequest(BaseModel):
    ProfileId: StrictStr
    InclusionAnnotation: Literal['INCLUDE', 'EXCLUDE']
