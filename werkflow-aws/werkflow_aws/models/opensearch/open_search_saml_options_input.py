from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .open_search_saml_idp import OpenSearchSAMLIdp


class OpenSearchSAMLOptionsInput(BaseModel):
    Enabled: StrictBool | None = None
    Idp: OpenSearchSAMLIdp | None = None
    MasterUserName: StrictStr | None = None
    MasterBackendRole: StrictStr | None = None
    SubjectKey: StrictStr | None = None
    RolesKey: StrictStr | None = None
    SessionTimeoutMinutes: StrictInt | None = None
