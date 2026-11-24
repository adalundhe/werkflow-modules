from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_login_profile import IAMLoginProfile


class IAMGetLoginProfileResponse(BaseModel):
    LoginProfile: IAMLoginProfile | None = None
    ResponseMetadata: dict[str, Any] | None = None
