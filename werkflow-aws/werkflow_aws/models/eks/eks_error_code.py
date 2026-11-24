from __future__ import annotations
from typing import Literal


EKSErrorCode = Literal[
    'SubnetNotFound',
    'SecurityGroupNotFound',
    'EniLimitReached',
    'IpNotAvailable',
    'AccessDenied',
    'OperationNotPermitted',
    'VpcIdNotFound',
    'Unknown',
    'NodeCreationFailure',
    'PodEvictionFailure',
    'InsufficientFreeAddresses',
    'ClusterUnreachable',
    'InsufficientNumberOfReplicas',
    'ConfigurationConflict',
    'AdmissionRequestDenied',
    'UnsupportedAddonModification',
    'K8sResourceNotFound',
]
