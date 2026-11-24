from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt
from .ec2_additional_key_exchange_methods_request_list_value import EC2AdditionalKeyExchangeMethodsRequestListValue


class EC2VpnAdditionalKeyExchangeRequest(BaseModel):
    AdditionalKeyExchangeRound: StrictInt
    KeyExchangeMethods: list[EC2AdditionalKeyExchangeMethodsRequestListValue] | None = None
    Requirement: Literal['required', 'optional'] | None = None
