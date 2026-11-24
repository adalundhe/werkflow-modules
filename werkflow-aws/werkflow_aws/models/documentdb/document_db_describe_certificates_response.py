from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_db_certificate import DocumentDBCertificate


class DocumentDBDescribeCertificatesResponse(BaseModel):
    Certificates: list[DocumentDBCertificate] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
