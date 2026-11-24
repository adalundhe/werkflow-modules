from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaCodeSigningPolicies(BaseModel):
    UntrustedArtifactOnDeployment: StrictStr | None = None
