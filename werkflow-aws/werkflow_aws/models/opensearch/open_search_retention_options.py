from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class OpenSearchRetentionOptions(BaseModel):
    RetentionInHours: StrictInt | None = None
    RetentionAction: StrictStr | None = None
