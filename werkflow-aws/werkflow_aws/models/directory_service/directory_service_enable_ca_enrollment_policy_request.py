from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceEnableCAEnrollmentPolicyRequest(BaseModel):
    DirectoryId: StrictStr
    PcaConnectorArn: StrictStr
