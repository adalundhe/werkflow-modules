from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .acme_account_summary import AcmeAccountSummary


class ACMListAcmeAccountsResponse(BaseModel):
    AcmeAccounts: list[AcmeAccountSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
