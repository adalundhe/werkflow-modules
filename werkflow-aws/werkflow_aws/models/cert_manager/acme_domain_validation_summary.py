from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .acm_failure_details import ACMFailureDetails
from .acm_prevalidation_details import ACMPrevalidationDetails


class AcmeDomainValidationSummary(BaseModel):
    AcmeDomainValidationArn: StrictStr | None = None
    AcmeEndpointArn: StrictStr | None = None
    DomainName: StrictStr | None = None
    PrevalidationType: StrictStr | None = None
    PrevalidationDetails: ACMPrevalidationDetails | None = None
    Status: StrictStr | None = None
    FailureDetails: ACMFailureDetails | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
