from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_s3_classification_scope_update import MacieS3ClassificationScopeUpdate


class MacieUpdateClassificationScopeRequest(BaseModel):
    id: StrictStr
    s3: MacieS3ClassificationScopeUpdate | None = None
