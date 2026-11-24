from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogUpdateConstraintRequest(BaseModel):
    Id: StrictStr
    AcceptLanguage: StrictStr | None = None
    Description: StrictStr | None = None
    Parameters: StrictStr | None = None
