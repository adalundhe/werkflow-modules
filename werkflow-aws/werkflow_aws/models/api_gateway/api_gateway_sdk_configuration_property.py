from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewaySdkConfigurationProperty(BaseModel):
    name: StrictStr | None = None
    friendlyName: StrictStr | None = None
    description: StrictStr | None = None
    required: StrictBool | None = None
    defaultValue: StrictStr | None = None
