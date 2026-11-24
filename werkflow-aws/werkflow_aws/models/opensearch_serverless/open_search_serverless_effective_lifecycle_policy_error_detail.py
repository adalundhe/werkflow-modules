from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessEffectiveLifecyclePolicyErrorDetail(BaseModel):
    type: StrictStr | None = None
    resource: StrictStr | None = None
    errorMessage: StrictStr | None = None
    errorCode: StrictStr | None = None
