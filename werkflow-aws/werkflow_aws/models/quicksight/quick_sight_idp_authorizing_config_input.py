from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .quick_sight_idc_trusted_token_issuer_config import QuickSightIdcTrustedTokenIssuerConfig
from .quick_sight_idp_authorizing_configuration_detail_input import QuickSightIdpAuthorizingConfigurationDetailInput


class QuickSightIdpAuthorizingConfigInput(BaseModel):
    IdpAuthorizingType: Literal['EXTERNAL_IDP_PUBLIC_AUTH_CODE', 'EXTERNAL_IDP_CONFIDENTIAL_AUTH_CODE', 'QUICK_MANAGED_AUTH_CODE', 'IDC_AUTH_CODE']
    IdpAuthorizingConfigurationDetailInput: QuickSightIdpAuthorizingConfigurationDetailInput | None = None
    IdcTrustedTokenIssuerConfiguration: QuickSightIdcTrustedTokenIssuerConfig | None = None
