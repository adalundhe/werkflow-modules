from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class CloudFormationStackInstanceFilter(BaseModel):
    Name: Literal['DETAILED_STATUS', 'LAST_OPERATION_ID', 'DRIFT_STATUS'] | None = None
    Values: StrictStr | None = None
