from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .app_runner_certificate_validation_record import AppRunnerCertificateValidationRecord


class AppRunnerCustomDomain(BaseModel):
    DomainName: StrictStr | None = None
    EnableWWWSubdomain: StrictBool | None = None
    CertificateValidationRecords: list[AppRunnerCertificateValidationRecord] | None = None
    Status: StrictStr | None = None
