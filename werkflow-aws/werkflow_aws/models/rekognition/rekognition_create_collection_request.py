from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionCreateCollectionRequest(BaseModel):
    CollectionId: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
