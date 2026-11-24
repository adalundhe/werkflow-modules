from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ServiceCatalogDescribeCopyProductStatusResponse(BaseModel):
    CopyProductStatus: StrictStr | None = None
    TargetProductId: StrictStr | None = None
    StatusDetail: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
