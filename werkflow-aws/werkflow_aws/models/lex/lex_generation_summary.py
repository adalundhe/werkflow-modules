from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LexGenerationSummary(BaseModel):
    generationId: StrictStr | None = None
    generationStatus: StrictStr | None = None
    creationDateTime: datetime.datetime | StrictStr | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
