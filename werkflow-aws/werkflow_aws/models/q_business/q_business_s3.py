from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessS3(BaseModel):
    bucket: StrictStr | None = None
    key: StrictStr | None = None
