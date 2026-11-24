from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSS3CreateBucketConfiguration(BaseModel):
    LocationConstraint: StrictStr | None = None
