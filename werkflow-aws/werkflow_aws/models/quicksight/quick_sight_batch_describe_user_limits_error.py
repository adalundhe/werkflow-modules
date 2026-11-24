from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightBatchDescribeUserLimitsError(BaseModel):
    userName: StrictStr | None = None
    namespace: StrictStr | None = None
    userArn: StrictStr | None = None
    errorCode: StrictStr | None = None
    message: StrictStr | None = None
