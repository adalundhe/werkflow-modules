from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_retrieval_configuration import MacieRetrievalConfiguration
from .macie_reveal_configuration import MacieRevealConfiguration


class MacieGetRevealConfigurationResponse(BaseModel):
    configuration: MacieRevealConfiguration | None = None
    retrievalConfiguration: MacieRetrievalConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
