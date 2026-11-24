from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .kms_grant_constraints import KMSGrantConstraints


class KMSCreateGrantRequest(BaseModel):
    KeyId: StrictStr
    Operations: list[Literal['Decrypt', 'Encrypt', 'GenerateDataKey', 'GenerateDataKeyWithoutPlaintext', 'ReEncryptFrom', 'ReEncryptTo', 'Sign', 'Verify', 'GetPublicKey', 'CreateGrant', 'RetireGrant', 'DescribeKey', 'GenerateDataKeyPair', 'GenerateDataKeyPairWithoutPlaintext', 'GenerateMac', 'VerifyMac', 'DeriveSharedSecret', 'Encapsulate', 'Decapsulate']]
    GranteePrincipal: StrictStr | None = None
    RetiringPrincipal: StrictStr | None = None
    Constraints: KMSGrantConstraints | None = None
    GrantTokens: list[StrictStr] | None = None
    Name: StrictStr | None = None
    DryRun: StrictBool | None = None
    GranteeServicePrincipal: StrictStr | None = None
    RetiringServicePrincipal: StrictStr | None = None
