from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class SESPutAccountDeliveryAttributesRequest(BaseModel):
    SharedPoolDeliveryMode: Literal['GLOBAL', 'REGIONAL']
