from __future__ import annotations
from pydantic import BaseModel
from .macie_s3_classification_scope_exclusion import MacieS3ClassificationScopeExclusion


class MacieS3ClassificationScope(BaseModel):
    excludes: MacieS3ClassificationScopeExclusion | None = None
