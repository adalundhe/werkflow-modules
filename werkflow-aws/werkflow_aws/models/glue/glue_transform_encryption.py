from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_ml_user_data_encryption import GlueMLUserDataEncryption


class GlueTransformEncryption(BaseModel):
    MlUserDataEncryption: GlueMLUserDataEncryption | None = None
    TaskRunSecurityConfigurationName: StrictStr | None = None
