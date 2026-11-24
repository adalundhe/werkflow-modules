from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceDisableCAEnrollmentPolicyRequest(BaseModel):
    DirectoryId: StrictStr
