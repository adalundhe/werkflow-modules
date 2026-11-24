from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class EndUserMessagingSendDestinationNumberVerificationCodeRequest(BaseModel):
    VerifiedDestinationNumberId: StrictStr
    VerificationChannel: Literal['TEXT', 'VOICE']
    LanguageCode: Literal['DE_DE', 'EN_GB', 'EN_US', 'ES_419', 'ES_ES', 'FR_CA', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW'] | None = None
    OriginationIdentity: StrictStr | None = None
    ConfigurationSetName: StrictStr | None = None
    Context: dict[StrictStr, StrictStr] | None = None
    DestinationCountryParameters: dict[Literal['IN_TEMPLATE_ID', 'IN_ENTITY_ID'], StrictStr] | None = None
