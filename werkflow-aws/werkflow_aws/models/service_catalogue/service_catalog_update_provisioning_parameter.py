from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ServiceCatalogUpdateProvisioningParameter(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    UsePreviousValue: StrictBool | None = None
