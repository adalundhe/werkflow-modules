from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IAMPolicyVersionModel(BaseModel):
    Document: StrictStr | None = None
    VersionId: StrictStr | None = None
    IsDefaultVersion: StrictBool | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
