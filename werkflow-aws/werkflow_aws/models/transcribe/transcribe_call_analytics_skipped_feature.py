from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TranscribeCallAnalyticsSkippedFeature(BaseModel):
    Feature: StrictStr | None = None
    ReasonCode: StrictStr | None = None
    Message: StrictStr | None = None
