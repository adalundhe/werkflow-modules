from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class TextractAdapterOverview(BaseModel):
    AdapterId: StrictStr | None = None
    AdapterName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FeatureTypes: list[StrictStr] | None = None
