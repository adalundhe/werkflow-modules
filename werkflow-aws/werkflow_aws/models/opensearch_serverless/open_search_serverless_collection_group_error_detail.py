from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessCollectionGroupErrorDetail(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    errorMessage: StrictStr | None = None
    errorCode: StrictStr | None = None
