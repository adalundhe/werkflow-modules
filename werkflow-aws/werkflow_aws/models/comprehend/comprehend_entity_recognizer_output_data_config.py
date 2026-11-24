from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendEntityRecognizerOutputDataConfig(BaseModel):
    FlywheelStatsS3Prefix: StrictStr | None = None
