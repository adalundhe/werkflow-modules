from __future__ import annotations
from pydantic import BaseModel
from .iam_access_key import IAMAccessKey


class IAMCreateAccessKeyResponse(BaseModel):
    AccessKey: IAMAccessKey | None = None
