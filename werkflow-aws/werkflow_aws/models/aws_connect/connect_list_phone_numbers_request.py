from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListPhoneNumbersRequest(BaseModel):
    InstanceId: StrictStr
    PhoneNumberTypes: list[Literal['TOLL_FREE', 'DID', 'UIFN', 'SHARED', 'THIRD_PARTY_TF', 'THIRD_PARTY_DID', 'SHORT_CODE']] | None = None
    PhoneNumberCountryCodes: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
