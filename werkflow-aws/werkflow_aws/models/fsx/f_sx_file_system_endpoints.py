from __future__ import annotations
from pydantic import BaseModel
from .f_sx_file_system_endpoint import FSxFileSystemEndpoint


class FSxFileSystemEndpoints(BaseModel):
    Intercluster: FSxFileSystemEndpoint | None = None
    Management: FSxFileSystemEndpoint | None = None
