from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_suppress_data_identifier import MacieSuppressDataIdentifier


class MacieUpdateResourceProfileDetectionsRequest(BaseModel):
    resourceArn: StrictStr
    suppressDataIdentifiers: list[MacieSuppressDataIdentifier] | None = None
