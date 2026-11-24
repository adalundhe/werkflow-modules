from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_api_call_details import MacieApiCallDetails


class MacieFindingAction(BaseModel):
    actionType: StrictStr | None = None
    apiCallDetails: MacieApiCallDetails | None = None
