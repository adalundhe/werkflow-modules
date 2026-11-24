from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_status_type import IAMStatusType


class IAMAccessKey(BaseModel):
    UserName: StrictStr | None = None
    AccessKeyId: StrictStr | None = None
    Status: IAMStatusType | None = None
    SecretAccessKey: StrictStr | None = None
    CreateDate: datetime.datetime | None = None
