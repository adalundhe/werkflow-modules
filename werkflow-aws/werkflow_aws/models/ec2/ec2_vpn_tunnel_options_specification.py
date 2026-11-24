from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_ike_versions_request_list_value import EC2IKEVersionsRequestListValue
from .ec2_phase1_dh_group_numbers_request_list_value import EC2Phase1DHGroupNumbersRequestListValue
from .ec2_phase1_encryption_algorithms_request_list_value import EC2Phase1EncryptionAlgorithmsRequestListValue
from .ec2_phase1_integrity_algorithms_request_list_value import EC2Phase1IntegrityAlgorithmsRequestListValue
from .ec2_phase2_dh_group_numbers_request_list_value import EC2Phase2DHGroupNumbersRequestListValue
from .ec2_phase2_encryption_algorithms_request_list_value import EC2Phase2EncryptionAlgorithmsRequestListValue
from .ec2_phase2_integrity_algorithms_request_list_value import EC2Phase2IntegrityAlgorithmsRequestListValue
from .ec2_vpn_additional_key_exchange_request import EC2VpnAdditionalKeyExchangeRequest
from .ec2_vpn_tunnel_log_options_specification import EC2VpnTunnelLogOptionsSpecification


class EC2VpnTunnelOptionsSpecification(BaseModel):
    TunnelInsideCidr: StrictStr | None = None
    TunnelInsideIpv6Cidr: StrictStr | None = None
    PreSharedKey: StrictStr | None = None
    Phase1LifetimeSeconds: StrictInt | None = None
    Phase2LifetimeSeconds: StrictInt | None = None
    RekeyMarginTimeSeconds: StrictInt | None = None
    RekeyFuzzPercentage: StrictInt | None = None
    ReplayWindowSize: StrictInt | None = None
    DPDTimeoutSeconds: StrictInt | None = None
    DPDTimeoutAction: StrictStr | None = None
    Phase1EncryptionAlgorithms: list[EC2Phase1EncryptionAlgorithmsRequestListValue] | None = None
    Phase2EncryptionAlgorithms: list[EC2Phase2EncryptionAlgorithmsRequestListValue] | None = None
    Phase1IntegrityAlgorithms: list[EC2Phase1IntegrityAlgorithmsRequestListValue] | None = None
    Phase2IntegrityAlgorithms: list[EC2Phase2IntegrityAlgorithmsRequestListValue] | None = None
    Phase1DHGroupNumbers: list[EC2Phase1DHGroupNumbersRequestListValue] | None = None
    Phase2DHGroupNumbers: list[EC2Phase2DHGroupNumbersRequestListValue] | None = None
    IKEVersions: list[EC2IKEVersionsRequestListValue] | None = None
    StartupAction: StrictStr | None = None
    LogOptions: EC2VpnTunnelLogOptionsSpecification | None = None
    EnableTunnelLifecycleControl: StrictBool | None = None
    Phase1AdditionalKeyExchanges: list[EC2VpnAdditionalKeyExchangeRequest] | None = None
    Phase2AdditionalKeyExchanges: list[EC2VpnAdditionalKeyExchangeRequest] | None = None
