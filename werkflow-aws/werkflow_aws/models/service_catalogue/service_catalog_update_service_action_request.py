from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogUpdateServiceActionRequest(BaseModel):
    Id: StrictStr
    Name: StrictStr | None = None
    Definition: dict[Literal['Name', 'Version', 'AssumeRole', 'Parameters'], StrictStr] | None = None
    Description: StrictStr | None = None
    AcceptLanguage: StrictStr | None = None
