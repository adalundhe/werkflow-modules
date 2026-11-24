from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessLifecyclePolicyErrorDetail(BaseModel):
    type: StrictStr | None = None
    name: StrictStr | None = None
    errorMessage: StrictStr | None = None
    errorCode: StrictStr | None = None
