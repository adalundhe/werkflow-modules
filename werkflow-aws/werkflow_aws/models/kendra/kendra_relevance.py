from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class KendraRelevance(BaseModel):
    Freshness: StrictBool | None = None
    Importance: StrictInt | None = None
    Duration: StrictStr | None = None
    RankOrder: StrictStr | None = None
    ValueImportanceMap: dict[StrictStr, StrictInt] | None = None
