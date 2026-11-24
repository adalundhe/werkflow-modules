from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_scanning_repository_filter import ECRScanningRepositoryFilter


class ECRRegistryScanningRule(BaseModel):
    scanFrequency: StrictStr | None = None
    repositoryFilters: list[ECRScanningRepositoryFilter] | None = None
