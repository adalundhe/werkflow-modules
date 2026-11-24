from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .iam_tag_model import IAMTagModel
from .iam_user_model import IAMUserModel


class IAMVirtualMFADevice(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    SerialNumber: StrictStr | None = None
    Base32StringSeed: StrictBytes | Any | None = None
    QRCodePNG: StrictBytes | Any | None = None
    User: IAMUserModel | None = None
    EnableDate: datetime.datetime | StrictStr | None = None
    Tags: list[IAMTagModel] | None = None
