from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class TaxSettingsPutTaxInheritanceRequest(BaseModel):
    heritageStatus: Literal['OptIn', 'OptOut'] | None = None
