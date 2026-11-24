from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerIamIdentity(BaseModel):
    Arn: StrictStr | None = None
    PrincipalId: StrictStr | None = None
    SourceIdentity: StrictStr | None = None
