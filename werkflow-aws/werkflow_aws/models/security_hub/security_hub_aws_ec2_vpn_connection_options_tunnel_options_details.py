from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEc2VpnConnectionOptionsTunnelOptionsDetails(BaseModel):
    DpdTimeoutSeconds: StrictInt | None = None
    IkeVersions: list[StrictStr] | None = None
    OutsideIpAddress: StrictStr | None = None
    Phase1DhGroupNumbers: list[StrictInt] | None = None
    Phase1EncryptionAlgorithms: list[StrictStr] | None = None
    Phase1IntegrityAlgorithms: list[StrictStr] | None = None
    Phase1LifetimeSeconds: StrictInt | None = None
    Phase2DhGroupNumbers: list[StrictInt] | None = None
    Phase2EncryptionAlgorithms: list[StrictStr] | None = None
    Phase2IntegrityAlgorithms: list[StrictStr] | None = None
    Phase2LifetimeSeconds: StrictInt | None = None
    PreSharedKey: StrictStr | None = None
    RekeyFuzzPercentage: StrictInt | None = None
    RekeyMarginTimeSeconds: StrictInt | None = None
    ReplayWindowSize: StrictInt | None = None
    TunnelInsideCidr: StrictStr | None = None
