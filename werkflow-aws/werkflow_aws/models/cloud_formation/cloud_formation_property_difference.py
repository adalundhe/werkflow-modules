from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationPropertyDifference(BaseModel):
    PropertyPath: StrictStr | None = None
    ExpectedValue: StrictStr | None = None
    ActualValue: StrictStr | None = None
    DifferenceType: StrictStr | None = None
