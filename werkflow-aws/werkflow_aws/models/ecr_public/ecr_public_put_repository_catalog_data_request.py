from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_public_repository_catalog_data_input import ECRPublicRepositoryCatalogDataInput


class ECRPublicPutRepositoryCatalogDataRequest(BaseModel):
    repositoryName: StrictStr
    catalogData: ECRPublicRepositoryCatalogDataInput
    registryId: StrictStr | None = None
