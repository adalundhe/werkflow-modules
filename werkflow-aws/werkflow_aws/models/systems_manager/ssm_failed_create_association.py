from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_create_association_batch_request_entry import SSMCreateAssociationBatchRequestEntry


class SSMFailedCreateAssociation(BaseModel):
    Entry: SSMCreateAssociationBatchRequestEntry | None = None
    Message: StrictStr | None = None
    Fault: StrictStr | None = None
