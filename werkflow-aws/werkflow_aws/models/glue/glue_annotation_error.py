from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAnnotationError(BaseModel):
    ProfileId: StrictStr | None = None
    StatisticId: StrictStr | None = None
    FailureReason: StrictStr | None = None
