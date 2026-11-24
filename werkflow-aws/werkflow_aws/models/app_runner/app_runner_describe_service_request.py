from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDescribeServiceRequest(BaseModel):
    ServiceArn: StrictStr
