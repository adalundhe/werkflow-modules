from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerTotalHits(BaseModel):
    Value: StrictInt | None = None
    Relation: StrictStr | None = None
