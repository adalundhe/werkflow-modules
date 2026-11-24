from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightGetSessionEmbedUrlRequest(BaseModel):
    AwsAccountId: StrictStr
    EntryPoint: StrictStr | None = None
    SessionLifetimeInMinutes: StrictInt | None = None
    UserArn: StrictStr | None = None
