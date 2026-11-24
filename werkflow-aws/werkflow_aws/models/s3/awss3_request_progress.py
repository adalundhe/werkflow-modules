from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AWSS3RequestProgress(BaseModel):
    Enabled: StrictBool | None = None
