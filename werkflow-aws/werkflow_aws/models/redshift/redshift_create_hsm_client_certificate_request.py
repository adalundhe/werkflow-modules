from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateHsmClientCertificateRequest(BaseModel):
    HsmClientCertificateIdentifier: StrictStr
    Tags: list[RedshiftTag] | None = None
