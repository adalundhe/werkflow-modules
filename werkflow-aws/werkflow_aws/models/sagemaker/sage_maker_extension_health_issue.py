from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerExtensionHealthIssue(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    NodeCount: StrictInt | None = None
