from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .iam_context_provider import IAMContextProvider
from .iam_tag_model import IAMTagModel


class IAMCreateSAMLProviderRequest(BaseModel):
    SAMLMetadataDocument: StrictStr
    Name: StrictStr
    Tags: list[IAMTagModel] | None = None
    AssertionEncryptionMode: Literal['Required', 'Allowed'] | None = None
    AddPrivateKey: StrictStr | None = None
    ContextProvider: IAMContextProvider | None = None
    IdentityCenterInstanceArn: StrictStr | None = None
