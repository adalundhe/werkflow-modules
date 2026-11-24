from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TextractAdapterVersionOverview(BaseModel):
    AdapterId: StrictStr | None = None
    AdapterVersion: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FeatureTypes: list[StrictStr] | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
