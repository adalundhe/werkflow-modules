from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_s3_classification_scope import MacieS3ClassificationScope


class MacieGetClassificationScopeResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    s3: MacieS3ClassificationScope | None = None
    ResponseMetadata: dict[str, Any] | None = None
