from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class SESPutAccountDetailsRequest(BaseModel):
    MailType: Literal['MARKETING', 'TRANSACTIONAL']
    WebsiteURL: StrictStr
    ContactLanguage: Literal['EN', 'JA'] | None = None
    UseCaseDescription: StrictStr | None = None
    AdditionalContactEmailAddresses: list[StrictStr] | None = None
    ProductionAccessEnabled: StrictBool | None = None
