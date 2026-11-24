from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_iam_identity import SageMakerIamIdentity


class SageMakerUserContext(BaseModel):
    UserProfileArn: StrictStr | None = None
    UserProfileName: StrictStr | None = None
    DomainId: StrictStr | None = None
    IamIdentity: SageMakerIamIdentity | None = None
