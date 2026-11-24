from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_idc_trusted_token_issuer_config import QuickSightIdcTrustedTokenIssuerConfig
from .quick_sight_idp_authorizing_configuration_summary_detail import QuickSightIdpAuthorizingConfigurationSummaryDetail


class QuickSightIdpAuthorizingConfigSummary(BaseModel):
    IdpAuthorizingType: StrictStr | None = None
    IdpAuthorizingConfigurationSummaryDetail: QuickSightIdpAuthorizingConfigurationSummaryDetail | None = None
    IdcTrustedTokenIssuerConfiguration: QuickSightIdcTrustedTokenIssuerConfig | None = None
