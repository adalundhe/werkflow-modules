from pydantic import (
    BaseModel,
    StrictStr,
    StrictBool,
)


class MSKS3(BaseModel):
    Bucket: StrictStr | None = None
    Enabled: StrictBool = False
    Prefix: StrictStr | None = None
    