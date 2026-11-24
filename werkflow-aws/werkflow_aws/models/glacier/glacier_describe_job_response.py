from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glacier_inventory_retrieval_job_description import GlacierInventoryRetrievalJobDescription
from .glacier_output_location import GlacierOutputLocation
from .glacier_select_parameters import GlacierSelectParameters


class GlacierDescribeJobResponse(BaseModel):
    JobId: StrictStr | None = None
    JobDescription: StrictStr | None = None
    Action: StrictStr | None = None
    ArchiveId: StrictStr | None = None
    VaultARN: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Completed: StrictBool | None = None
    StatusCode: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    ArchiveSizeInBytes: StrictInt | None = None
    InventorySizeInBytes: StrictInt | None = None
    SNSTopic: StrictStr | None = None
    CompletionDate: StrictStr | None = None
    SHA256TreeHash: StrictStr | None = None
    ArchiveSHA256TreeHash: StrictStr | None = None
    RetrievalByteRange: StrictStr | None = None
    Tier: StrictStr | None = None
    InventoryRetrievalParameters: GlacierInventoryRetrievalJobDescription | None = None
    JobOutputPath: StrictStr | None = None
    SelectParameters: GlacierSelectParameters | None = None
    OutputLocation: GlacierOutputLocation | None = None
    ResponseMetadata: dict[str, Any] | None = None
