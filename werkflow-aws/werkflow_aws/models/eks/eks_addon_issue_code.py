from __future__ import annotations
from typing import Literal


EKSAddonIssueCode = Literal[
    'AccessDenied',
    'InternalFailure',
    'ClusterUnreachable',
    'InsufficientNumberOfReplicas',
    'ConfigurationConflict',
    'AdmissionRequestDenied',
    'UnsupportedAddonModification',
    'K8sResourceNotFound',
    'AddonSubscriptionNeeded',
    'AddonPermissionFailure',
]
