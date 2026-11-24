from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_lifecycle_policy_preview_result import ECRLifecyclePolicyPreviewResult
from .ecr_lifecycle_policy_preview_summary import ECRLifecyclePolicyPreviewSummary


class ECRGetLifecyclePolicyPreviewResponse(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    lifecyclePolicyText: StrictStr | None = None
    status: StrictStr | None = None
    nextToken: StrictStr | None = None
    previewResults: list[ECRLifecyclePolicyPreviewResult] | None = None
    summary: ECRLifecyclePolicyPreviewSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
