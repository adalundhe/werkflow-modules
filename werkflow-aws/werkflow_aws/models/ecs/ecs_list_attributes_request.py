from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ECSListAttributesRequest(BaseModel):
    targetType: Literal['container-instance']
    cluster: StrictStr | None = None
    attributeName: StrictStr | None = None
    attributeValue: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
