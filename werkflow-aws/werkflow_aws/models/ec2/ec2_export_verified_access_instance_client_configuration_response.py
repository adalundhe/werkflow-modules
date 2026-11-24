from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_verified_access_instance_open_vpn_client_configuration import EC2VerifiedAccessInstanceOpenVpnClientConfiguration
from .ec2_verified_access_instance_user_trust_provider_client_configuration import EC2VerifiedAccessInstanceUserTrustProviderClientConfiguration


class EC2ExportVerifiedAccessInstanceClientConfigurationResponse(BaseModel):
    Version: StrictStr | None = None
    VerifiedAccessInstanceId: StrictStr | None = None
    Region: StrictStr | None = None
    DeviceTrustProviders: list[StrictStr] | None = None
    UserTrustProvider: EC2VerifiedAccessInstanceUserTrustProviderClientConfiguration | None = None
    OpenVpnConfigurations: list[EC2VerifiedAccessInstanceOpenVpnClientConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
