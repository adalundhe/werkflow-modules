from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightRestoreAnalysisResponse(BaseModel):
    Status: StrictInt | None = None
    Arn: StrictStr | None = None
    AnalysisId: StrictStr | None = None
    RequestId: StrictStr | None = None
    RestorationFailedFolderArns: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
