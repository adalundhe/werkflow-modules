from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerAnalyzedResourceSummary(BaseModel):
    resourceArn: StrictStr | None = None
    resourceOwnerAccount: StrictStr | None = None
    resourceType: StrictStr | None = None
