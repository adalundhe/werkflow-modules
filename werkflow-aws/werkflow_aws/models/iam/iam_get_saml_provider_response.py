from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .iam_context_provider import IAMContextProvider
from .iamsaml_key_hash_entry import IAMSAMLKeyHashEntry
from .iamsaml_private_key import IAMSAMLPrivateKey
from .iam_tag_model import IAMTagModel


class IAMGetSAMLProviderResponse(BaseModel):
    SAMLProviderUUID: StrictStr | None = None
    SAMLMetadataDocument: StrictStr | None = None
    ContextProvider: IAMContextProvider | None = None
    SAMLKeyHashes: list[IAMSAMLKeyHashEntry] | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    Tags: list[IAMTagModel] | None = None
    AssertionEncryptionMode: StrictStr | None = None
    PrivateKeyList: list[IAMSAMLPrivateKey] | None = None
    IdentityCenterInstanceArn: StrictStr | None = None
    IdentityStoreArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
