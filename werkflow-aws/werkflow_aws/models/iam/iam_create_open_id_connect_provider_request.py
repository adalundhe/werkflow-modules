from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_context_provider import IAMContextProvider
from .iam_tag_model import IAMTagModel


class IAMCreateOpenIDConnectProviderRequest(BaseModel):
    Url: StrictStr
    ClientIDList: list[StrictStr] | None = None
    ThumbprintList: list[StrictStr] | None = None
    Tags: list[IAMTagModel] | None = None
    ContextProvider: IAMContextProvider | None = None
    IdentityCenterInstanceArn: StrictStr | None = None
