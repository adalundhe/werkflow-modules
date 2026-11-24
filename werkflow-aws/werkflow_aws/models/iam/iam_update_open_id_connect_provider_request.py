from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_context_provider import IAMContextProvider


class IAMUpdateOpenIDConnectProviderRequest(BaseModel):
    OpenIDConnectProviderArn: StrictStr
    ContextProvider: IAMContextProvider | None = None
    IdentityCenterInstanceArn: StrictStr | None = None
    RemoveContextProvider: StrictBool | None = None
    RemoveIdentityCenterInstance: StrictBool | None = None
