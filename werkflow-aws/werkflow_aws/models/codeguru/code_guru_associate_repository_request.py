from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_guru_kms_key_details import CodeGuruKMSKeyDetails
from .code_guru_repository import CodeGuruRepository


class CodeGuruAssociateRepositoryRequest(BaseModel):
    Repository: CodeGuruRepository
    ClientRequestToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    KMSKeyDetails: CodeGuruKMSKeyDetails | None = None
