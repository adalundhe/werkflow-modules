from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_additional_key_exchange_methods_list_value import EC2AdditionalKeyExchangeMethodsListValue


class EC2VpnAdditionalKeyExchange(BaseModel):
    AdditionalKeyExchangeRound: StrictInt | None = None
    KeyExchangeMethods: list[EC2AdditionalKeyExchangeMethodsListValue] | None = None
    Requirement: StrictStr | None = None
