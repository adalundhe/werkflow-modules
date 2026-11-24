from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRegistryListItem(BaseModel):
    RegistryName: StrictStr | None = None
    RegistryArn: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    UpdatedTime: StrictStr | None = None
