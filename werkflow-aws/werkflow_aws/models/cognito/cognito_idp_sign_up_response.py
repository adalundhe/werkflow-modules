from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .cognito_idp_code_delivery_details_type import CognitoIDPCodeDeliveryDetailsType


class CognitoIDPSignUpResponse(BaseModel):
    UserConfirmed: StrictBool | None = None
    CodeDeliveryDetails: CognitoIDPCodeDeliveryDetailsType | None = None
    UserSub: StrictStr | None = None
    Session: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
