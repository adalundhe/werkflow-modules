from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DmsTransferSettings(BaseModel):
    ServiceAccessRoleArn: StrictStr | None = None
    BucketName: StrictStr | None = None
