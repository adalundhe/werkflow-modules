from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_retriever_configuration import QBusinessRetrieverConfiguration


class QBusinessUpdateRetrieverRequest(BaseModel):
    applicationId: StrictStr
    retrieverId: StrictStr
    configuration: QBusinessRetrieverConfiguration | None = None
    displayName: StrictStr | None = None
    roleArn: StrictStr | None = None
