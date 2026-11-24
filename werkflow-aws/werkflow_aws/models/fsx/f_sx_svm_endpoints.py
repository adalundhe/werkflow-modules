from __future__ import annotations
from pydantic import BaseModel
from .f_sx_svm_endpoint import FSxSvmEndpoint


class FSxSvmEndpoints(BaseModel):
    Iscsi: FSxSvmEndpoint | None = None
    Management: FSxSvmEndpoint | None = None
    Nfs: FSxSvmEndpoint | None = None
    Smb: FSxSvmEndpoint | None = None
