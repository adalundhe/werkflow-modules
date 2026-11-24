from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationDescribeTypeRegistrationRequest(BaseModel):
    RegistrationToken: StrictStr
