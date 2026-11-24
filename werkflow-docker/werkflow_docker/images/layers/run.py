import re
from typing import Any, Dict, Literal, Optional, Type, cast

from pydantic import BaseModel, StrictStr

from .mount_types import (
    BindMount,
    CacheMount,
    SSHMount,
    SecretMount,
    TMPFSMount,
)

MountType = BindMount | CacheMount | SecretMount | SSHMount | TMPFSMount
MountClassType = (
    Type[BindMount]
    | Type[CacheMount]
    | Type[SecretMount]
    | Type[SSHMount]
    | Type[TMPFSMount]
)


class Run(BaseModel):
    layer_type: Literal['run'] = 'run'
    command: StrictStr
    mount: Optional[MountType] = None
    network: Optional[Literal['default', 'host', 'none']] = None
    security: Optional[Literal['insecure', 'sandbox']] = None

    def to_string(self) -> str:
        run_string = 'RUN'

        if self.mount:
            mount_string = self.mount.to_string()
            run_string = f'{run_string} {mount_string}'

        if self.network:
            run_string = f'{run_string} --network={self.network}'

        if self.security:
            run_string = f'{run_string} --security={self.security}'

        return f'{run_string} {self.command}'

    @classmethod
    def parse(cls, line: str) -> 'Run':
        stripped = re.sub(r'^RUN\s+', '', line.strip(), count=1, flags=re.IGNORECASE).strip()
        tokens = stripped.split()

        options: Dict[str, Any] = {}

        for token in tokens:
            if token.startswith('--mount='):
                mount_token = token[len('--mount='):]
                options['mount'] = cls._parse_mount(mount_token)
                stripped = re.sub(re.escape(token), '', stripped, count=1).strip()
            elif token.startswith('--network='):
                options['network'] = cls._parse_network(token)
                stripped = re.sub(re.escape(token), '', stripped, count=1).strip()
            elif token.startswith('--security='):
                options['security'] = cls._parse_security(token)
                stripped = re.sub(re.escape(token), '', stripped, count=1).strip()
            else:
                break

        return cls(
            command=stripped.strip(),
            **options,
        )

    @classmethod
    def _parse_mount(cls, token: str) -> MountType:
        mount_type = 'bind'

        mount_types: Dict[str, MountClassType] = {
            'bind': BindMount,
            'cache': CacheMount,
            'secret': SecretMount,
            'ssh': SSHMount,
            'tmpfs': TMPFSMount,
        }

        if mount_match := re.search(r'type=(bind|cache|secret|ssh|tmpfs)', token):
            mount_type = mount_match.group(1)
            token = re.sub(r'type=(bind|cache|secret|ssh|tmpfs),?', '', token, count=1)

        return mount_types[mount_type].parse(token)

    @classmethod
    def _parse_network(cls, token: str) -> Literal['default', 'host', 'none']:
        if network := re.search(r'default|host|none', token):
            return cast(Literal['default', 'host', 'none'], network.group(0))
        return 'none'

    @classmethod
    def _parse_security(cls, token: str) -> Literal['insecure', 'sandbox']:
        if security := re.search(r'insecure|sandbox', token):
            return cast(Literal['insecure', 'sandbox'], security.group(0))
        return 'insecure'
