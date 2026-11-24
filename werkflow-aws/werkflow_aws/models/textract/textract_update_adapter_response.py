from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class TextractUpdateAdapterResponse(BaseModel):
    AdapterId: StrictStr | None = None
    AdapterName: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    FeatureTypes: list[StrictStr] | None = None
    AutoUpdate: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
