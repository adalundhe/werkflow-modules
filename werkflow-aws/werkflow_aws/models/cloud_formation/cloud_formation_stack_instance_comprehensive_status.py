from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationStackInstanceComprehensiveStatus(BaseModel):
    DetailedStatus: StrictStr | None = None
