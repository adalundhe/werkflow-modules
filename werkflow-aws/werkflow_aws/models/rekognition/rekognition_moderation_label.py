from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RekognitionModerationLabel(BaseModel):
    Confidence: StrictFloat | StrictInt | None = None
    Name: StrictStr | None = None
    ParentName: StrictStr | None = None
    TaxonomyLevel: StrictInt | None = None
