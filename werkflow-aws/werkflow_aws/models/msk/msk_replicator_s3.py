from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKReplicatorS3(BaseModel):
    Enabled: StrictBool | None = None
    Bucket: StrictStr | None = None
    Prefix: StrictStr | None = None
