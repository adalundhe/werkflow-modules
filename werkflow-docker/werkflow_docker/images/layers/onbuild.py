import re
from typing import Dict, Literal, Optional, Type

from pydantic import BaseModel, ConfigDict

from .add import Add
from .arg import Arg
from .cmd import Cmd
from .copy import Copy
from .entrypoint import Entrypoint
from .env import Env
from .expose import Expose
from .healthcheck import Healthcheck
from .label import Label
from .run import Run
from .shell import Shell
from .stopsignal import StopSignal
from .user import User
from .volume import Volume
from .workdir import Workdir

OnBuildInstruction = (
    Add
    | Arg
    | Cmd
    | Copy
    | Entrypoint
    | Env
    | Expose
    | Healthcheck
    | Label
    | Run
    | Shell
    | StopSignal
    | User
    | Volume
    | Workdir
)

OnBuildInstructionClass = (
    Type[Add]
    | Type[Arg]
    | Type[Cmd]
    | Type[Copy]
    | Type[Entrypoint]
    | Type[Env]
    | Type[Expose]
    | Type[Healthcheck]
    | Type[Label]
    | Type[Run]
    | Type[Shell]
    | Type[StopSignal]
    | Type[User]
    | Type[Volume]
    | Type[Workdir]
)


class OnBuild(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    layer_type: Literal['onbuild'] = 'onbuild'
    instruction: OnBuildInstruction

    def to_string(self) -> str:
        instruction_command = self.instruction.to_string()
        return f'ONBUILD {instruction_command}'

    @classmethod
    def parse(cls, line: str) -> Optional['OnBuild']:
        stripped = re.sub(
            r'^ONBUILD\s+',
            '',
            line.strip(),
            count=1,
            flags=re.IGNORECASE,
        ).strip()

        directives: Dict[str, OnBuildInstructionClass] = {
            'ADD': Add,
            'ARG': Arg,
            'CMD': Cmd,
            'COPY': Copy,
            'ENTRYPOINT': Entrypoint,
            'ENV': Env,
            'EXPOSE': Expose,
            'HEALTHCHECK': Healthcheck,
            'LABEL': Label,
            'RUN': Run,
            'SHELL': Shell,
            'STOPSIGNAL': StopSignal,
            'USER': User,
            'VOLUME': Volume,
            'WORKDIR': Workdir,
        }

        if directive_match := re.match(
            r'^(ADD|ARG|CMD|COPY|ENTRYPOINT|ENV|EXPOSE|HEALTHCHECK|LABEL|RUN|SHELL|STOPSIGNAL|USER|VOLUME|WORKDIR)\b',
            stripped,
            flags=re.IGNORECASE,
        ):
            directive_name = directive_match.group(1).upper()
            directive_cls = directives[directive_name]
            parsed_instruction = directive_cls.parse(stripped)
            return cls(instruction=parsed_instruction)

        return None
