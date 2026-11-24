from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .open_search_saml_idp import OpenSearchSAMLIdp


class OpenSearchSAMLOptionsOutput(BaseModel):
    Enabled: StrictBool | None = None
    Idp: OpenSearchSAMLIdp | None = None
    SubjectKey: StrictStr | None = None
    RolesKey: StrictStr | None = None
    SessionTimeoutMinutes: StrictInt | None = None
