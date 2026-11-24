from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectSearchAvailablePhoneNumbersRequest(BaseModel):
    PhoneNumberCountryCode: StrictStr
    PhoneNumberType: Literal['TOLL_FREE', 'DID', 'UIFN', 'SHARED', 'THIRD_PARTY_TF', 'THIRD_PARTY_DID', 'SHORT_CODE']
    TargetArn: StrictStr | None = None
    InstanceId: StrictStr | None = None
    PhoneNumberPrefix: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
