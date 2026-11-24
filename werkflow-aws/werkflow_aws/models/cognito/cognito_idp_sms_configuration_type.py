from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cognito_idp_eums_sms_configuration_type import CognitoIDPEumsSmsConfigurationType


class CognitoIDPSmsConfigurationType(BaseModel):
    SnsCallerArn: StrictStr | None = None
    ExternalId: StrictStr | None = None
    SnsRegion: StrictStr | None = None
    EumsSms: CognitoIDPEumsSmsConfigurationType | None = None
