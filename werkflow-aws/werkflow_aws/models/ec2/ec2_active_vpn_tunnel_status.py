from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_active_vpn_tunnel_additional_key_exchange import EC2ActiveVpnTunnelAdditionalKeyExchange


class EC2ActiveVpnTunnelStatus(BaseModel):
    Phase1EncryptionAlgorithm: StrictStr | None = None
    Phase2EncryptionAlgorithm: StrictStr | None = None
    Phase1IntegrityAlgorithm: StrictStr | None = None
    Phase2IntegrityAlgorithm: StrictStr | None = None
    Phase1DHGroup: StrictInt | None = None
    Phase2DHGroup: StrictInt | None = None
    IkeVersion: StrictStr | None = None
    ProvisioningStatus: StrictStr | None = None
    ProvisioningStatusReason: StrictStr | None = None
    Phase1AdditionalKeyExchanges: list[EC2ActiveVpnTunnelAdditionalKeyExchange] | None = None
    Phase2AdditionalKeyExchanges: list[EC2ActiveVpnTunnelAdditionalKeyExchange] | None = None
