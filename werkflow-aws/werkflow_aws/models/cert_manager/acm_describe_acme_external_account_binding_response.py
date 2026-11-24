from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acme_external_account_binding import AcmeExternalAccountBinding


class ACMDescribeAcmeExternalAccountBindingResponse(BaseModel):
    ExternalAccountBinding: AcmeExternalAccountBinding | None = None
    ResponseMetadata: dict[str, Any] | None = None
