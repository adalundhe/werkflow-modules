from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueTimestampedInclusionAnnotation(BaseModel):
    Value: StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
