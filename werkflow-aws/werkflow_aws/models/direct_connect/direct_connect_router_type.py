from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectRouterType(BaseModel):
    vendor: StrictStr | None = None
    platform: StrictStr | None = None
    software: StrictStr | None = None
    xsltTemplateName: StrictStr | None = None
    xsltTemplateNameForMacSec: StrictStr | None = None
    routerTypeIdentifier: StrictStr | None = None
