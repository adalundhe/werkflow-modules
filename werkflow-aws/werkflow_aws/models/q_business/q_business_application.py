from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .q_business_quick_sight_configuration import QBusinessQuickSightConfiguration


class QBusinessApplication(BaseModel):
    displayName: StrictStr | None = None
    applicationId: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    identityType: StrictStr | None = None
    quickSightConfiguration: QBusinessQuickSightConfiguration | None = None
