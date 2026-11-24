from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AWSS3DeleteObjectAnnotationResponse(BaseModel):
    ObjectVersionId: StrictStr | None = None
    RequestCharged: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
