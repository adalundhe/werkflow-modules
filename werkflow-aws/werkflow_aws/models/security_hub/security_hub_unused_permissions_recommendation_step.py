from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SecurityHubUnusedPermissionsRecommendationStep(BaseModel):
    RecommendedAction: StrictStr | None = None
    ExistingPolicy: StrictStr | None = None
    ExistingPolicyId: StrictStr | None = None
    PolicyUpdatedAt: datetime.datetime | StrictStr | None = None
    RecommendedPolicy: StrictStr | None = None
