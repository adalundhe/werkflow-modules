from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTS3Action(BaseModel):
    roleArn: StrictStr | None = None
    bucketName: StrictStr | None = None
    key: StrictStr | None = None
    cannedAcl: StrictStr | None = None
