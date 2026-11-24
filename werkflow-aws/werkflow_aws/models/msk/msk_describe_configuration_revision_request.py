from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKDescribeConfigurationRevisionRequest(BaseModel):
    Arn: StrictStr
    Revision: StrictInt
