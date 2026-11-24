from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogCopyProductRequest(BaseModel):
    SourceProductArn: StrictStr
    IdempotencyToken: StrictStr
    AcceptLanguage: StrictStr | None = None
    TargetProductId: StrictStr | None = None
    TargetProductName: StrictStr | None = None
    SourceProvisioningArtifactIdentifiers: list[dict[Literal['Id'], StrictStr]] | None = None
    CopyOptions: list[Literal['CopyTags']] | None = None
