from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightAssetBundleImportJobAnalysisOverrideParameters(BaseModel):
    AnalysisId: StrictStr | None = None
    Name: StrictStr | None = None
