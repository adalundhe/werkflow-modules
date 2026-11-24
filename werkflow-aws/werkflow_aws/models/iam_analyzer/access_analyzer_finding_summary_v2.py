from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AccessAnalyzerFindingSummaryV2(BaseModel):
    analyzedAt: datetime.datetime | StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    error: StrictStr | None = None
    id: StrictStr | None = None
    resource: StrictStr | None = None
    resourceType: StrictStr | None = None
    resourceOwnerAccount: StrictStr | None = None
    status: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    findingType: StrictStr | None = None
