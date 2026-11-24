from __future__ import annotations
from pydantic import BaseModel
from .f_sx_open_zfs_client_configuration import FSxOpenZFSClientConfiguration


class FSxOpenZFSNfsExport(BaseModel):
    ClientConfigurations: list[FSxOpenZFSClientConfiguration] | None = None
