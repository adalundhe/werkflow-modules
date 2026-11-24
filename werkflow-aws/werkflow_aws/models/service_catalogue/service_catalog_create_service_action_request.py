from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ServiceCatalogCreateServiceActionRequest(BaseModel):
    Name: StrictStr
    DefinitionType: Literal['SSM_AUTOMATION']
    Definition: dict[Literal['Name', 'Version', 'AssumeRole', 'Parameters'], StrictStr]
    IdempotencyToken: StrictStr
    Description: StrictStr | None = None
    AcceptLanguage: StrictStr | None = None
