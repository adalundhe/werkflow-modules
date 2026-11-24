from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionGeneralLabelsSettings(BaseModel):
    LabelInclusionFilters: list[StrictStr] | None = None
    LabelExclusionFilters: list[StrictStr] | None = None
    LabelCategoryInclusionFilters: list[StrictStr] | None = None
    LabelCategoryExclusionFilters: list[StrictStr] | None = None
