from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class PersonalizeCreateBatchSegmentJobResponse(BaseModel):
    batchSegmentJobArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
