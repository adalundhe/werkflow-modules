from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowSuccessResponseHandlingConfig(BaseModel):
    bucketPrefix: StrictStr | None = None
    bucketName: StrictStr | None = None
