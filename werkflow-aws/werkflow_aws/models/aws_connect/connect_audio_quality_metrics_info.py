from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ConnectAudioQualityMetricsInfo(BaseModel):
    QualityScore: StrictFloat | StrictInt | None = None
    PotentialQualityIssues: list[StrictStr] | None = None
