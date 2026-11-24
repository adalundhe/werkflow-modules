from __future__ import annotations
from typing import Literal


EKSUpdateType = Literal[
    'VersionUpdate',
    'EndpointAccessUpdate',
    'LoggingUpdate',
    'ConfigUpdate',
    'AssociateIdentityProviderConfig',
    'DisassociateIdentityProviderConfig',
    'AssociateEncryptionConfig',
    'AddonUpdate',
    'VpcConfigUpdate',
    'AccessConfigUpdate',
    'UpgradePolicyUpdate',
    'ZonalShiftConfigUpdate',
    'AutoModeUpdate',
    'RemoteNetworkConfigUpdate',
    'DeletionProtectionUpdate',
    'CapabilityUpdate',
    'ControlPlaneScalingConfigUpdate',
    'VendedLogsUpdate',
    'ControlPlaneEgressUpdate',
    'VersionRollback',
    'ControlPlaneComponentConfigUpdate',
    'CertificateAuthorityUpdate',
]
