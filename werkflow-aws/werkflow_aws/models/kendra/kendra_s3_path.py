from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraS3Path(BaseModel):
    Bucket: StrictStr | None = None
    Key: StrictStr | None = None
