from __future__ import annotations
from pydantic import BaseModel
from .rds_scalar_reference_details import RDSScalarReferenceDetails


class RDSReferenceDetails(BaseModel):
    ScalarReferenceDetails: RDSScalarReferenceDetails | None = None
