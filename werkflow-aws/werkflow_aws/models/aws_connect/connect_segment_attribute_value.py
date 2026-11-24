from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectSegmentAttributeValue(BaseModel):
    ValueString: StrictStr | None = None
    ValueMap: dict[StrictStr, ConnectSegmentAttributeValue] | None = None
    ValueInteger: StrictInt | None = None
    ValueList: list[ConnectSegmentAttributeValue] | None = None
    ValueArn: StrictStr | None = None
