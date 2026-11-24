from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_context_provider import IAMContextProvider


class IAMUpdateSAMLProviderRequest(BaseModel):
    SAMLProviderArn: StrictStr
    SAMLMetadataDocument: StrictStr | None = None
    AssertionEncryptionMode: Literal['Required', 'Allowed'] | None = None
    AddPrivateKey: StrictStr | None = None
    RemovePrivateKey: StrictStr | None = None
    ContextProvider: IAMContextProvider | None = None
    IdentityCenterInstanceArn: StrictStr | None = None
    RemoveContextProvider: StrictBool | None = None
    RemoveIdentityCenterInstance: StrictBool | None = None
