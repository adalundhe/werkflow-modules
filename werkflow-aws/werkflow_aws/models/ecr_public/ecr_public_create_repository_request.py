from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_public_repository_catalog_data_input import ECRPublicRepositoryCatalogDataInput
from .ecr_public_tag import ECRPublicTag


class ECRPublicCreateRepositoryRequest(BaseModel):
    repositoryName: StrictStr
    catalogData: ECRPublicRepositoryCatalogDataInput | None = None
    tags: list[ECRPublicTag] | None = None
