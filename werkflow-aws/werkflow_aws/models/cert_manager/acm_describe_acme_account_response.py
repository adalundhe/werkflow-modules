from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acme_account import AcmeAccount as _AcmeAccountType


class ACMDescribeAcmeAccountResponse(BaseModel):
    AcmeAccount: _AcmeAccountType | None = None
    ResponseMetadata: dict[str, Any] | None = None
