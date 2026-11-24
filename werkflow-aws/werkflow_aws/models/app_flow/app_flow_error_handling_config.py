from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppFlowErrorHandlingConfig(BaseModel):
    failOnFirstDestinationError: StrictBool | None = None
    bucketPrefix: StrictStr | None = None
    bucketName: StrictStr | None = None
