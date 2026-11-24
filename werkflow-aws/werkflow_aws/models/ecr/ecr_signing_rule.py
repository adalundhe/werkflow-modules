from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_signing_repository_filter import ECRSigningRepositoryFilter


class ECRSigningRule(BaseModel):
    signingProfileArn: StrictStr | None = None
    repositoryFilters: list[ECRSigningRepositoryFilter] | None = None
