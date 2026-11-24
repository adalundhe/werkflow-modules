from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .q_business_retriever_configuration import QBusinessRetrieverConfiguration
from .q_business_tag import QBusinessTag


class QBusinessCreateRetrieverRequest(BaseModel):
    applicationId: StrictStr
    type: Literal['NATIVE_INDEX', 'KENDRA_INDEX']
    displayName: StrictStr
    configuration: QBusinessRetrieverConfiguration
    roleArn: StrictStr | None = None
    clientToken: StrictStr | None = None
    tags: list[QBusinessTag] | None = None
