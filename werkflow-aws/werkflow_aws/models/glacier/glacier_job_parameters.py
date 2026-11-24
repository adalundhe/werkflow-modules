from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glacier_inventory_retrieval_job_input import GlacierInventoryRetrievalJobInput
from .glacier_output_location import GlacierOutputLocation
from .glacier_select_parameters import GlacierSelectParameters


class GlacierJobParameters(BaseModel):
    Format: StrictStr | None = None
    Type: StrictStr | None = None
    ArchiveId: StrictStr | None = None
    Description: StrictStr | None = None
    SNSTopic: StrictStr | None = None
    RetrievalByteRange: StrictStr | None = None
    Tier: StrictStr | None = None
    InventoryRetrievalParameters: GlacierInventoryRetrievalJobInput | None = None
    SelectParameters: GlacierSelectParameters | None = None
    OutputLocation: GlacierOutputLocation | None = None
