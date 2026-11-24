from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAssociateTargetsWithJobRequest(BaseModel):
    targets: list[StrictStr]
    jobId: StrictStr
    comment: StrictStr | None = None
    namespaceId: StrictStr | None = None
