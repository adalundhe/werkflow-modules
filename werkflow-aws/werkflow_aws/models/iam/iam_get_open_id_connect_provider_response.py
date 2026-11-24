from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .iam_context_provider import IAMContextProvider
from .iam_tag_model import IAMTagModel


class IAMGetOpenIDConnectProviderResponse(BaseModel):
    Url: StrictStr | None = None
    ClientIDList: list[StrictStr] | None = None
    ThumbprintList: list[StrictStr] | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    Tags: list[IAMTagModel] | None = None
    ContextProvider: IAMContextProvider | None = None
    IdentityCenterInstanceArn: StrictStr | None = None
    IdentityStoreArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
