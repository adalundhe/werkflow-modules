from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_assumed_role_user import STSAssumedRoleUser
from .sts_credentials import STSCredentials
from .sts_trusted_identity_propagation_context import STSTrustedIdentityPropagationContext


class STSAssumeRoleWithSAMLResponse(BaseModel):
    Credentials: STSCredentials | None = None
    AssumedRoleUser: STSAssumedRoleUser | None = None
    PackedPolicySize: StrictInt | None = None
    Subject: StrictStr | None = None
    SubjectType: StrictStr | None = None
    Issuer: StrictStr | None = None
    Audience: StrictStr | None = None
    NameQualifier: StrictStr | None = None
    SourceIdentity: StrictStr | None = None
    SessionTokenUtilization: StrictInt | None = None
    SessionTokenSize: StrictInt | None = None
    TrustedIdentityPropagationContext: STSTrustedIdentityPropagationContext | None = None
    ResponseMetadata: dict[str, Any] | None = None
