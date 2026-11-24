from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerCreateDomainResponse(BaseModel):
    DomainArn: StrictStr | None = None
    DomainId: StrictStr | None = None
    Url: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
