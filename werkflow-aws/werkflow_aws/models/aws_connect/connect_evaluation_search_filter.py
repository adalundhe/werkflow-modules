from __future__ import annotations
from pydantic import BaseModel
from .connect_contact_evaluation_attribute_filter import ConnectContactEvaluationAttributeFilter
from .connect_control_plane_attribute_filter import ConnectControlPlaneAttributeFilter


class ConnectEvaluationSearchFilter(BaseModel):
    AttributeFilter: ConnectControlPlaneAttributeFilter | None = None
    ContactEvaluationAttributeFilter: ConnectContactEvaluationAttributeFilter | None = None
