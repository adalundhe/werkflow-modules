from pydantic import (
    BaseModel,
    StrictStr,
)


class AthenaAclConfiguration(BaseModel):
    S3AclOption: StrictStr