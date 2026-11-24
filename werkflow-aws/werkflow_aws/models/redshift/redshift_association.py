from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .redshift_certificate_association import RedshiftCertificateAssociation


class RedshiftAssociation(BaseModel):
    CustomDomainCertificateArn: StrictStr | None = None
    CustomDomainCertificateExpiryDate: datetime.datetime | StrictStr | None = None
    CertificateAssociations: list[RedshiftCertificateAssociation] | None = None
