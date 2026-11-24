from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeCAEnrollmentPolicyRequest(BaseModel):
    DirectoryId: StrictStr
