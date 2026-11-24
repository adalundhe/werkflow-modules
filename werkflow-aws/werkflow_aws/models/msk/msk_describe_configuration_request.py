from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDescribeConfigurationRequest(BaseModel):
    Arn: StrictStr | None = None
