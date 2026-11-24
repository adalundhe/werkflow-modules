from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SESPutAccountPricingAttributesRequest(BaseModel):
    Plan: Literal['NONE', 'ESSENTIALS', 'PRO', 'ENTERPRISE']
