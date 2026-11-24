from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPKeyConfigurationType(BaseModel):
    KeyType: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
