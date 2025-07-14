from pydantic import BaseModel, StrictStr


class MSKEncryptionAtRest(BaseModel):
    DataVolumeMKSKeyId: StrictStr