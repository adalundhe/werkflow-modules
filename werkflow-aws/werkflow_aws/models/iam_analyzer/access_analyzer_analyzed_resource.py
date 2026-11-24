from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class AccessAnalyzerAnalyzedResource(BaseModel):
    resourceArn: StrictStr | None = None
    resourceType: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    analyzedAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    isPublic: StrictBool | None = None
    actions: list[StrictStr] | None = None
    sharedVia: list[StrictStr] | None = None
    status: StrictStr | None = None
    resourceOwnerAccount: StrictStr | None = None
    error: StrictStr | None = None
