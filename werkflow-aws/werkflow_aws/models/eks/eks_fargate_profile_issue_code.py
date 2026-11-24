from __future__ import annotations
from typing import Literal


EKSFargateProfileIssueCode = Literal[
    'PodExecutionRoleAlreadyInUse',
    'AccessDenied',
    'ClusterUnreachable',
    'InternalFailure',
]
