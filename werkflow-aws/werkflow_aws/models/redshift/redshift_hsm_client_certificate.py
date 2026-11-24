from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftHsmClientCertificate(BaseModel):
    HsmClientCertificateIdentifier: StrictStr | None = None
    HsmClientCertificatePublicKey: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
