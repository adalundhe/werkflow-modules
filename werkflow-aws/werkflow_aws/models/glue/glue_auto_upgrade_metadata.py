from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueAutoUpgradeMetadata(BaseModel):
    TargetVersion: StrictStr | None = None
    SourceVersion: StrictStr | None = None
    Status: StrictStr | None = None
    AnalysisId: StrictStr | None = None
