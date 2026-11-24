from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class LexAggregatedUtterancesSummary(BaseModel):
    utterance: StrictStr | None = None
    hitCount: StrictInt | None = None
    missedCount: StrictInt | None = None
    utteranceFirstRecordedInAggregationDuration: datetime.datetime | StrictStr | None = None
    utteranceLastRecordedInAggregationDuration: datetime.datetime | StrictStr | None = None
    containsDataFromDeletedResources: StrictBool | None = None
