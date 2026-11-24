from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_timestamped_inclusion_annotation import GlueTimestampedInclusionAnnotation


class GlueStatisticAnnotation(BaseModel):
    ProfileId: StrictStr | None = None
    StatisticId: StrictStr | None = None
    StatisticRecordedOn: datetime.datetime | StrictStr | None = None
    InclusionAnnotation: GlueTimestampedInclusionAnnotation | None = None
