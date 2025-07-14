from pydantic import (
    BaseModel,
    StrictBool,
    StrictStr,
)


class MSKFirehose(BaseModel):
    DeliveryStream: StrictStr | None = None
    Enabled: StrictBool = False
    