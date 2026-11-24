import json
import re
from typing import List, Literal, Optional

from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class Shell(BaseModel):
    layer_type: Literal['shell'] = 'shell'
    executable: StrictStr
    parameters: Optional[
        List[StrictBool | StrictFloat | StrictInt | StrictStr]
    ] = None

    def to_string(self) -> str:
        shell_command_args: List[str] = [self.executable]

        if self.parameters:
            shell_command_args.extend(
                parameter if isinstance(parameter, str) else str(parameter)
                for parameter in self.parameters
            )

        return f'SHELL {json.dumps(shell_command_args)}'

    @classmethod
    def parse(cls, line: str) -> 'Shell':
        stripped = re.sub(r'^SHELL\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()

        command: List[str] = []
        if stripped.startswith('['):
            try:
                parsed = json.loads(stripped)
                if isinstance(parsed, list):
                    command = [str(item) for item in parsed]
            except json.JSONDecodeError:
                pass

        if not command:
            command = [
                arg.strip().strip('"').strip("'")
                for arg in re.sub(r'^\[|\]$', '', stripped).split(',')
                if arg.strip()
            ]

        parameters: Optional[List[StrictBool | StrictFloat | StrictInt | StrictStr]] = None
        if len(command) > 1:
            parameters = list(command[1:])

        return cls(
            executable=command[0],
            parameters=parameters,
        )
