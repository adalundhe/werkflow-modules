from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceExternalEvaluation(BaseModel):
    ComplianceResourceType: StrictStr
    ComplianceResourceId: StrictStr
    ComplianceType: Literal['COMPLIANT', 'NON_COMPLIANT', 'NOT_APPLICABLE', 'INSUFFICIENT_DATA']
    OrderingTimestamp: datetime.datetime | StrictStr
    Annotation: StrictStr | None = None
