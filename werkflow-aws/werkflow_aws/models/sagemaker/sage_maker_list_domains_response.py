from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_domain_details import SageMakerDomainDetails


class SageMakerListDomainsResponse(BaseModel):
    Domains: list[SageMakerDomainDetails] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
