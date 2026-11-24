from __future__ import annotations
import datetime
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr


class KMSImportKeyMaterialRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    KeyId: StrictStr
    ImportToken: StrictBytes | BinaryIO | StrictStr
    EncryptedKeyMaterial: StrictBytes | BinaryIO | StrictStr
    ValidTo: datetime.datetime | StrictStr | None = None
    ExpirationModel: Literal['KEY_MATERIAL_EXPIRES', 'KEY_MATERIAL_DOES_NOT_EXPIRE'] | None = None
    ImportType: Literal['NEW_KEY_MATERIAL', 'EXISTING_KEY_MATERIAL'] | None = None
    KeyMaterialDescription: StrictStr | None = None
    KeyMaterialId: StrictStr | None = None
