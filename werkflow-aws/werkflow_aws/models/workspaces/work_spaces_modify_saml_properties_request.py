from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_saml_properties import WorkSpacesSamlProperties


class WorkSpacesModifySamlPropertiesRequest(BaseModel):
    ResourceId: StrictStr
    SamlProperties: WorkSpacesSamlProperties | None = None
    PropertiesToDelete: list[Literal['SAML_PROPERTIES_USER_ACCESS_URL', 'SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME']] | None = None
