from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .quick_sight_idc_trusted_token_issuer_config import QuickSightIdcTrustedTokenIssuerConfig
from .quick_sight_idp_authorizing_configuration_detail_update_input import QuickSightIdpAuthorizingConfigurationDetailUpdateInput


class QuickSightIdpAuthorizingConfigUpdateInput(BaseModel):
    IdpAuthorizingType: Literal['EXTERNAL_IDP_PUBLIC_AUTH_CODE', 'EXTERNAL_IDP_CONFIDENTIAL_AUTH_CODE', 'QUICK_MANAGED_AUTH_CODE', 'IDC_AUTH_CODE']
    IdpAuthorizingConfigurationDetailInput: QuickSightIdpAuthorizingConfigurationDetailUpdateInput | None = None
    IdcTrustedTokenIssuerConfiguration: QuickSightIdcTrustedTokenIssuerConfig | None = None
