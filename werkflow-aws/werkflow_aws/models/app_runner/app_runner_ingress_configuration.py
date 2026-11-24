from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AppRunnerIngressConfiguration(BaseModel):
    IsPubliclyAccessible: StrictBool | None = None
