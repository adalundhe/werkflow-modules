from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ike_versions_list_value import EC2IKEVersionsListValue
from .ec2_phase1_dh_group_numbers_list_value import EC2Phase1DHGroupNumbersListValue
from .ec2_phase1_encryption_algorithms_list_value import EC2Phase1EncryptionAlgorithmsListValue
from .ec2_phase1_integrity_algorithms_list_value import EC2Phase1IntegrityAlgorithmsListValue
from .ec2_phase2_dh_group_numbers_list_value import EC2Phase2DHGroupNumbersListValue
from .ec2_phase2_encryption_algorithms_list_value import EC2Phase2EncryptionAlgorithmsListValue
from .ec2_phase2_integrity_algorithms_list_value import EC2Phase2IntegrityAlgorithmsListValue
from .ec2_vpn_additional_key_exchange import EC2VpnAdditionalKeyExchange
from .ec2_vpn_tunnel_log_options import EC2VpnTunnelLogOptions


class EC2TunnelOption(BaseModel):
    OutsideIpAddress: StrictStr | None = None
    TunnelInsideCidr: StrictStr | None = None
    TunnelInsideIpv6Cidr: StrictStr | None = None
    PreSharedKey: StrictStr | None = None
    Phase1LifetimeSeconds: StrictInt | None = None
    Phase2LifetimeSeconds: StrictInt | None = None
    RekeyMarginTimeSeconds: StrictInt | None = None
    RekeyFuzzPercentage: StrictInt | None = None
    ReplayWindowSize: StrictInt | None = None
    DpdTimeoutSeconds: StrictInt | None = None
    DpdTimeoutAction: StrictStr | None = None
    Phase1EncryptionAlgorithms: list[EC2Phase1EncryptionAlgorithmsListValue] | None = None
    Phase2EncryptionAlgorithms: list[EC2Phase2EncryptionAlgorithmsListValue] | None = None
    Phase1IntegrityAlgorithms: list[EC2Phase1IntegrityAlgorithmsListValue] | None = None
    Phase2IntegrityAlgorithms: list[EC2Phase2IntegrityAlgorithmsListValue] | None = None
    Phase1DHGroupNumbers: list[EC2Phase1DHGroupNumbersListValue] | None = None
    Phase2DHGroupNumbers: list[EC2Phase2DHGroupNumbersListValue] | None = None
    IkeVersions: list[EC2IKEVersionsListValue] | None = None
    StartupAction: StrictStr | None = None
    LogOptions: EC2VpnTunnelLogOptions | None = None
    EnableTunnelLifecycleControl: StrictBool | None = None
    Phase1AdditionalKeyExchanges: list[EC2VpnAdditionalKeyExchange] | None = None
    Phase2AdditionalKeyExchanges: list[EC2VpnAdditionalKeyExchange] | None = None
