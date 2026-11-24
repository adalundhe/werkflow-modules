from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteAnalysisResponse(BaseModel):
    Status: StrictInt | None = None
    Arn: StrictStr | None = None
    AnalysisId: StrictStr | None = None
    DeletionTime: datetime.datetime | StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
