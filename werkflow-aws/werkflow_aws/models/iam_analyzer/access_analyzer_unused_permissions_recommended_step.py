from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AccessAnalyzerUnusedPermissionsRecommendedStep(BaseModel):
    policyUpdatedAt: datetime.datetime | StrictStr | None = None
    recommendedAction: StrictStr | None = None
    recommendedPolicy: StrictStr | None = None
    existingPolicyId: StrictStr | None = None
