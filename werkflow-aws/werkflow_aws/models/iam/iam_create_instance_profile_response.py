from __future__ import annotations
from pydantic import BaseModel
from .iam_instance_profile import IAMInstanceProfile


class IAMCreateInstanceProfileResponse(BaseModel):
    InstanceProfile: IAMInstanceProfile | None = None
