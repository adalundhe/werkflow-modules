from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystListSpacesRequest(BaseModel):
    nextToken: StrictStr | None = None
