from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .code_catalyst_execute_command_session_configuration import CodeCatalystExecuteCommandSessionConfiguration


class CodeCatalystDevEnvironmentSessionConfiguration(BaseModel):
    sessionType: Literal['SSM', 'SSH']
    executeCommandSessionConfiguration: CodeCatalystExecuteCommandSessionConfiguration | None = None
