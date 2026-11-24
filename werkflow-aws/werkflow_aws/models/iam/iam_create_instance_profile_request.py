from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_tag import IAMTag


class IAMCreateInstanceProfileRequest(BaseModel):
    InstanceProfileName: StrictStr
    Path: StrictStr | None = None
    Tags: list[IAMTag] | None = None
