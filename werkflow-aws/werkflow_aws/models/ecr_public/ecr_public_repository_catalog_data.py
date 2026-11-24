from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECRPublicRepositoryCatalogData(BaseModel):
    description: StrictStr | None = None
    architectures: list[StrictStr] | None = None
    operatingSystems: list[StrictStr] | None = None
    logoUrl: StrictStr | None = None
    aboutText: StrictStr | None = None
    usageText: StrictStr | None = None
    marketplaceCertified: StrictBool | None = None
