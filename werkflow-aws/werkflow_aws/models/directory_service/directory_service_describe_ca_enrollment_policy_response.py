from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class DirectoryServiceDescribeCAEnrollmentPolicyResponse(BaseModel):
    DirectoryId: StrictStr | None = None
    PcaConnectorArn: StrictStr | None = None
    CaEnrollmentPolicyStatus: StrictStr | None = None
    LastUpdatedDateTime: datetime.datetime | StrictStr | None = None
    CaEnrollmentPolicyStatusReason: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
