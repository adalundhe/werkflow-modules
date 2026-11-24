from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_challenge_javascript_sdk_injection_config import WAFv2ChallengeJavascriptSdkInjectionConfig
from .wa_fv2_request_body_associated_resource_type_config import WAFv2RequestBodyAssociatedResourceTypeConfig


class WAFv2AssociationConfig(BaseModel):
    RequestBody: dict[StrictStr, WAFv2RequestBodyAssociatedResourceTypeConfig] | None = None
    ChallengeJavascriptSdkInjection: dict[StrictStr, WAFv2ChallengeJavascriptSdkInjectionConfig] | None = None
