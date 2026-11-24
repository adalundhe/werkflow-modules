from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .q_business_text_segment import QBusinessTextSegment


class QBusinessSourceAttribution(BaseModel):
    title: StrictStr | None = None
    snippet: StrictStr | None = None
    url: StrictStr | None = None
    citationNumber: StrictInt | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    textMessageSegments: list[QBusinessTextSegment] | None = None
    documentId: StrictStr | None = None
    indexId: StrictStr | None = None
    datasourceId: StrictStr | None = None
