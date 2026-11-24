from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ecr_scanning_repository_filter import ECRScanningRepositoryFilter


class ECRRepositoryScanningConfiguration(BaseModel):
    repositoryArn: StrictStr | None = None
    repositoryName: StrictStr | None = None
    scanOnPush: StrictBool | None = None
    scanFrequency: StrictStr | None = None
    appliedScanFilters: list[ECRScanningRepositoryFilter] | None = None
