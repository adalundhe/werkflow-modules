from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListThingsRequest(BaseModel):
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    attributeName: StrictStr | None = None
    attributeValue: StrictStr | None = None
    thingTypeName: StrictStr | None = None
    usePrefixAttributeValue: StrictBool | None = None
