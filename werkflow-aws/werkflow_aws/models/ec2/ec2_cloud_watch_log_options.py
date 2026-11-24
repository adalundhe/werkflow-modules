from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2CloudWatchLogOptions(BaseModel):
    LogEnabled: StrictBool | None = None
    LogGroupArn: StrictStr | None = None
    LogOutputFormat: StrictStr | None = None
    BgpLogEnabled: StrictBool | None = None
    BgpLogGroupArn: StrictStr | None = None
    BgpLogOutputFormat: StrictStr | None = None
