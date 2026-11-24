from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceEvaluation(BaseModel):
    ComplianceResourceType: StrictStr | None = None
    ComplianceResourceId: StrictStr | None = None
    ComplianceType: StrictStr | None = None
    Annotation: StrictStr | None = None
    OrderingTimestamp: datetime.datetime | StrictStr | None = None
