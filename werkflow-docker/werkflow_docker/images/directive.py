import re
from enum import Enum
from typing import Dict, Iterator, List, Literal, Optional, Sequence, Type, cast

from .layers import (
    Add,
    Arg,
    Cmd,
    Copy,
    Entrypoint,
    Env,
    Expose,
    Healthcheck,
    Label,
    Maintainer,
    OnBuild,
    Run,
    Shell,
    Stage,
    StopSignal,
    User,
    Volume,
    Workdir,
)

DirectiveName = Literal[
    'ADD',
    'ARG',
    'CMD',
    'COPY',
    'ENTRYPOINT',
    'ENV',
    'EXPOSE',
    'FROM',
    'HEALTHCHECK',
    'LABEL',
    'MAINTAINER',
    'ONBUILD',
    'RUN',
    'SHELL',
    'STOPSIGNAL',
    'USER',
    'VOLUME',
    'WORKDIR',
]

LayerType = (
    Add
    | Arg
    | Cmd
    | Copy
    | Entrypoint
    | Env
    | Expose
    | Healthcheck
    | Label
    | Maintainer
    | OnBuild
    | Run
    | Shell
    | Stage
    | StopSignal
    | User
    | Volume
    | Workdir
)

LayerClassType = (
    Type[Add]
    | Type[Arg]
    | Type[Cmd]
    | Type[Copy]
    | Type[Entrypoint]
    | Type[Env]
    | Type[Expose]
    | Type[Healthcheck]
    | Type[Label]
    | Type[Maintainer]
    | Type[OnBuild]
    | Type[Run]
    | Type[Shell]
    | Type[Stage]
    | Type[StopSignal]
    | Type[User]
    | Type[Volume]
    | Type[Workdir]
)


class Directive(Enum):
    ADD = 'ADD'
    ARG = 'ARG'
    CMD = 'CMD'
    COPY = 'COPY'
    ENTRYPOINT = 'ENTRYPOINT'
    ENV = 'ENV'
    EXPOSE = 'EXPOSE'
    FROM = 'FROM'
    HEALTHCHECK = 'HEALTHCHECK'
    LABEL = 'LABEL'
    MAINTAINER = 'MAINTAINER'
    ONBUILD = 'ONBUILD'
    RUN = 'RUN'
    SHELL = 'SHELL'
    STOPSIGNAL = 'STOPSIGNAL'
    USER = 'USER'
    VOLUME = 'VOLUME'
    WORKDIR = 'WORKDIR'


class Directives:

    def __init__(self) -> None:
        self._directives: Dict[DirectiveName, Directive] = {
            'ADD': Directive.ADD,
            'ARG': Directive.ARG,
            'CMD': Directive.CMD,
            'COPY': Directive.COPY,
            'ENTRYPOINT': Directive.ENTRYPOINT,
            'ENV': Directive.ENV,
            'EXPOSE': Directive.EXPOSE,
            'FROM': Directive.FROM,
            'HEALTHCHECK': Directive.HEALTHCHECK,
            'LABEL': Directive.LABEL,
            'MAINTAINER': Directive.MAINTAINER,
            'ONBUILD': Directive.ONBUILD,
            'RUN': Directive.RUN,
            'SHELL': Directive.SHELL,
            'STOPSIGNAL': Directive.STOPSIGNAL,
            'USER': Directive.USER,
            'VOLUME': Directive.VOLUME,
            'WORKDIR': Directive.WORKDIR,
        }

        self._layers: Dict[Directive, LayerClassType] = {
            Directive.ADD: Add,
            Directive.ARG: Arg,
            Directive.CMD: Cmd,
            Directive.COPY: Copy,
            Directive.ENTRYPOINT: Entrypoint,
            Directive.ENV: Env,
            Directive.EXPOSE: Expose,
            Directive.FROM: Stage,
            Directive.HEALTHCHECK: Healthcheck,
            Directive.LABEL: Label,
            Directive.MAINTAINER: Maintainer,
            Directive.ONBUILD: OnBuild,
            Directive.RUN: Run,
            Directive.SHELL: Shell,
            Directive.STOPSIGNAL: StopSignal,
            Directive.USER: User,
            Directive.VOLUME: Volume,
            Directive.WORKDIR: Workdir,
        }

        self._directive_names = list(self._directives.keys())
        self._directives_pattern = re.compile(
            r'^\s*(' + '|'.join(self._directive_names) + r')(?:\s|$)',
            re.IGNORECASE,
        )
        self._file_data: List[str] = []
        self._docker_file_lines: List[str] = []

    def __iter__(self) -> Iterator[DirectiveName]:
        for directive_name in self._directives:
            yield directive_name

    def __getitem__(self, directive_name: DirectiveName) -> Directive:
        return self._directives[directive_name]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Directives):
            return self._directives == other._directives
        return NotImplemented

    def __contains__(self, item: object) -> bool:
        if not isinstance(item, str):
            return False
        if item.upper() in self._directives:
            return True
        return self.from_file_line(item) is not None

    def parse(
        self,
        dockerfile: str | bytes | Sequence[str] | Sequence[bytes],
    ) -> List[LayerType]:
        self._file_data = []
        self._docker_file_lines = []

        if isinstance(dockerfile, str):
            self._file_data.extend(dockerfile.splitlines())
        elif isinstance(dockerfile, bytes):
            self._file_data.extend(dockerfile.decode().splitlines())
        else:
            for line in dockerfile:
                decoded = line.decode() if isinstance(line, bytes) else line
                self._file_data.append(decoded.rstrip('\r\n'))

        self._file_data = [
            line
            for line in self._file_data
            if not line.strip().startswith('#') and len(line.strip()) > 0
        ]

        if len(self._file_data) == 0:
            return []

        current_line = self._file_data[0]
        for line in self._file_data[1:]:
            if current_line.rstrip().endswith('\\'):
                current_line = f'{current_line}\n{line}'
            elif self.from_file_line(line):
                self._docker_file_lines.append(str(current_line))
                current_line = line
            else:
                current_line += f' {line.strip()}'

        self._docker_file_lines.append(current_line)

        docker_directives: List[LayerType] = []
        for docker_file_line in self._docker_file_lines:
            if directive := self.parse_directive(docker_file_line):
                docker_directives.append(directive)

        return docker_directives

    def from_file_line(self, directive_line: str) -> Optional[DirectiveName]:
        if matches := self._directives_pattern.match(directive_line):
            return cast(DirectiveName, matches.group(1).upper())
        return None

    def parse_directive(self, directive_line: str) -> Optional[LayerType]:
        if directive_name := self.from_file_line(directive_line):
            directive_type = self._directives[directive_name]
            return self._layers[directive_type].parse(directive_line)
        return None
