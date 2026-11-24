from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rds_reference_details import RDSReferenceDetails


class RDSMetricReference(BaseModel):
    Name: StrictStr | None = None
    ReferenceDetails: RDSReferenceDetails | None = None
