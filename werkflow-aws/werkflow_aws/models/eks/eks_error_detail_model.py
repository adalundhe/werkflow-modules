from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSErrorDetailModel(BaseModel):
    errorCode: StrictStr | None = None
    errorMessage: StrictStr | None = None
    resourceIds: list[StrictStr] | None = None
