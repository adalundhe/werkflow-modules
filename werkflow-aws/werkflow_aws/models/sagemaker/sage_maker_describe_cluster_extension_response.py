from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sage_maker_extension_details import SageMakerExtensionDetails
from .sage_maker_extension_health import SageMakerExtensionHealth
from .sage_maker_extension_node_summary import SageMakerExtensionNodeSummary


class SageMakerDescribeClusterExtensionResponse(BaseModel):
    ExtensionDetails: SageMakerExtensionDetails | None = None
    NodeSummary: SageMakerExtensionNodeSummary | None = None
    Health: SageMakerExtensionHealth | None = None
    ResponseMetadata: dict[str, Any] | None = None
