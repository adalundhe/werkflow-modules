from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_ontap_error import FSxOntapError


class FSxLifecycleTransitionReason(BaseModel):
    Message: StrictStr | None = None
    OntapError: FSxOntapError | None = None
