from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IAMPolicyVersion(BaseModel):
    Document: StrictStr | None = None
    VersionId: StrictStr | None = None
    IsDefaultVersion: StrictBool | None = None
    CreateDate: datetime.datetime | None = None
