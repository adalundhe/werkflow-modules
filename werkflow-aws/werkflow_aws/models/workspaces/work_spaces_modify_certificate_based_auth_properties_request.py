from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_certificate_based_auth_properties import WorkSpacesCertificateBasedAuthProperties


class WorkSpacesModifyCertificateBasedAuthPropertiesRequest(BaseModel):
    ResourceId: StrictStr
    CertificateBasedAuthProperties: WorkSpacesCertificateBasedAuthProperties | None = None
    PropertiesToDelete: list[Literal['CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN']] | None = None
