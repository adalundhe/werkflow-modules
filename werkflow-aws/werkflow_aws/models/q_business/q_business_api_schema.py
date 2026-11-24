from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_s3 import QBusinessS3


class QBusinessAPISchema(BaseModel):
    payload: StrictStr | None = None
    s3: QBusinessS3 | None = None
