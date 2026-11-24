from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMComplianceItemEntry(BaseModel):
    Severity: Literal['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFORMATIONAL', 'UNSPECIFIED']
    Status: Literal['COMPLIANT', 'NON_COMPLIANT']
    Id: StrictStr | None = None
    Title: StrictStr | None = None
    Details: dict[StrictStr, StrictStr] | None = None
