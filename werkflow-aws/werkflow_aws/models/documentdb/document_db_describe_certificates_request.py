from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .document_db_filter import DocumentDBFilter


class DocumentDBDescribeCertificatesRequest(BaseModel):
    CertificateIdentifier: StrictStr | None = None
    Filters: list[DocumentDBFilter] | None = None
    MaxRecords: StrictInt | None = None
    Marker: StrictStr | None = None
