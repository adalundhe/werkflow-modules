from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2GetTopPathStatisticsByTrafficRequest(BaseModel):
    WebAclArn: StrictStr
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    TimeWindow: WAFv2TimeWindow
    Limit: StrictInt
    NumberOfTopTrafficBotsPerPath: StrictInt
    UriPathPrefix: StrictStr | None = None
    BotCategory: StrictStr | None = None
    BotOrganization: StrictStr | None = None
    BotName: StrictStr | None = None
    NextMarker: StrictStr | None = None
