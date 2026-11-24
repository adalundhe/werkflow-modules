from __future__ import annotations
from typing import Literal


EKSClusterIssueCode = Literal[
    'AccessDenied',
    'ClusterUnreachable',
    'ConfigurationConflict',
    'InternalFailure',
    'ResourceLimitExceeded',
    'ResourceNotFound',
    'IamRoleNotFound',
    'VpcNotFound',
    'InsufficientFreeAddresses',
    'Ec2ServiceNotSubscribed',
    'Ec2SubnetNotFound',
    'Ec2SecurityGroupNotFound',
    'KmsGrantRevoked',
    'KmsKeyNotFound',
    'KmsKeyMarkedForDeletion',
    'KmsKeyDisabled',
    'StsRegionalEndpointDisabled',
    'UnsupportedVersion',
    'Other',
]
