from __future__ import annotations

import os
import pathlib
import re
import tarfile
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Literal,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)

from .directive import Directives, LayerType
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
from .layers.mount_types import (
    BindMount,
    CacheMount,
    SSHMount,
    SecretMount,
    TMPFSMount,
)
from .memory_file import MemoryFile
from .queries import LayerQuery

LayerKind = Literal[
    'add',
    'arg',
    'cmd',
    'copy',
    'entrypoint',
    'env',
    'expose',
    'healthcheck',
    'label',
    'maintainer',
    'onbuild',
    'run',
    'shell',
    'stage',
    'stopsignal',
    'user',
    'volume',
    'workdir',
]


class Image:

    def __init__(
        self,
        name: str,
        tag: str = 'latest',
        filename: Optional[str] = None,
        path: Optional[str] = None,
    ) -> None:
        self.name = name
        self.tag = tag
        self.path = path
        self.files: List[str] = []

        if filename is None:
            stub = name.replace('/', '.')
            filename = f'Dockerfile.{stub}'

        self.filename = filename
        self._layers: List[LayerType] = []

        self._mount_types: Dict[
            str,
            Callable[
                [Dict[str, Any]],
                Union[
                    BindMount,
                    CacheMount,
                    SecretMount,
                    SSHMount,
                    TMPFSMount,
                ],
            ],
        ] = {
            'bind': lambda config: BindMount(**config),
            'cache': lambda config: CacheMount(**config),
            'secret': lambda config: SecretMount(**config),
            'ssh': lambda config: SSHMount(**config),
            'tmpfs': lambda config: TMPFSMount(**config),
        }

        self.directives = Directives()
        self._variable_template_pattern = re.compile(
            r'(\$\{)([^\}]+)\}|(\$)([\w]+)'
        )

        self._variable_resolved_name_pattern = re.compile(
            r'(?<=\$\{).+?(?=:-|\})|(?<=\$)([\w]+)'
        )

        self._variable_clean_pattern = re.compile(r'\$|\{|\}')

    @property
    def full_name(self) -> str:
        return f'{self.name}:{self.tag}'

    def __iter__(self) -> Iterator[LayerType]:
        for layer in self._layers:
            yield layer

    @classmethod
    def generate_from_file(
        cls,
        filepath: str,
        output_path: Optional[str] = None,
    ) -> Image:
        directives = Directives()
        filename = pathlib.Path(filepath).name

        with open(filepath) as dockerfile:
            layers = directives.parse(dockerfile.readlines())

        image_sources: List[Stage] = [
            layer for layer in layers if isinstance(layer, Stage)
        ]

        if output_path:
            filename = output_path

        if len(image_sources) < 1:
            image = Image(
                'Unknown',
                filename=filename,
                path=output_path,
            )
            image.from_layers(layers)
            return image

        image_source = image_sources[-1]
        image = Image(
            image_source.base,
            tag=image_source.tag,
            filename=filename,
            path=output_path,
        )
        image.from_layers(layers)
        return image

    @classmethod
    def generate_from_string(
        cls,
        dockerfile: str | bytes | Sequence[str] | Sequence[bytes],
        filename: Optional[str] = None,
        output_path: Optional[str] = None,
    ) -> Image:
        directives = Directives()
        layers = directives.parse(dockerfile)

        image_sources: List[Stage] = [
            layer for layer in layers if isinstance(layer, Stage)
        ]

        if output_path:
            filename = output_path

        if len(image_sources) < 1:
            image = Image(
                'Unknown',
                filename=filename,
                path=output_path,
            )
            image.from_layers(layers)
            return image

        image_source = image_sources[-1]
        image = Image(
            image_source.base,
            tag=image_source.tag,
            filename=filename,
            path=output_path,
        )
        image.from_layers(layers)
        return image

    def from_string(self, dockerfile: str) -> Image:
        self._layers.extend(self.directives.parse(dockerfile))
        return self

    def from_file(self, filepath: str) -> Image:
        filename = pathlib.Path(filepath).name
        self.filename = filename

        with open(filepath) as dockerfile:
            self._layers.extend(self.directives.parse(dockerfile.readlines()))

        return self

    def from_layers(self, layers: Optional[List[LayerType]] = None) -> Image:
        self._layers = list(layers) if layers is not None else []
        return self

    def layers(
        self,
        layer_types: Optional[LayerKind | List[LayerKind]] = None,
        attribute: Optional[Tuple[str, Any]] = None,
    ) -> LayerQuery:
        filtered_layers: List[LayerType] = self._layers

        if layer_types is not None:
            requested_types = (
                layer_types if isinstance(layer_types, list) else [layer_types]
            )
            filtered_layers = [
                layer
                for layer in self._layers
                if layer.layer_type in requested_types
            ]

        query = LayerQuery(filtered_layers)

        if attribute is not None:
            attribute_name, attribute_value = attribute
            return query.get((attribute_name, attribute_value))

        return query

    def resolve(
        self,
        defaults: Optional[Dict[str, str]] = None,
        skip: Optional[List[str]] = None,
    ) -> Image:
        resolved_args = self.get_resolved_args()
        if defaults:
            resolved_args.update(defaults)

        skip_set = set(skip) if skip else set()
        resolved_args = {
            arg: value
            for arg, value in resolved_args.items()
            if arg not in skip_set
        }

        layers: List[LayerType] = list(self._layers)

        for idx, layer in enumerate(layers):
            if isinstance(layer, Arg):
                layer_data = layer.model_dump()
                layer_data['default'] = resolved_args.get(
                    layer.name,
                    layer.default,
                )
                layers[idx] = Arg(**layer_data)
            elif isinstance(layer, Env):
                values = [
                    resolved_args.get(key, layer.values[key_idx])
                    for key_idx, key in enumerate(layer.keys)
                ]
                layer_data = layer.model_dump()
                layer_data['values'] = values
                layers[idx] = Env(**layer_data)

        image = Image(
            self.name,
            tag=self.tag,
            filename=self.filename,
            path=self.path,
        )
        image.from_layers(layers)

        resolved_layers: List[LayerType] = []
        for layer in image:
            if not isinstance(layer, (Arg, Env)):
                layer = self._resolve_layer(layer, resolved_args)
            resolved_layers.append(layer)

        image.from_layers(resolved_layers)
        return image

    def get_resolved_args(self) -> Dict[str, Any]:
        arg_values: Dict[str, Any] = {}
        arg_layers = self.layers(layer_types='arg')
        for layer in arg_layers:
            if not isinstance(layer, Arg):
                continue

            arg_name = re.sub(self._variable_clean_pattern, '', layer.name)

            if arg_values.get(arg_name) is None and layer.default is not None:
                if not isinstance(layer.default, str) or not re.search(
                    self._variable_template_pattern,
                    layer.default,
                ):
                    arg_values[arg_name] = layer.default

        resolved_args: Dict[str, Any] = {}
        for arg_name in arg_values:
            resolved_args[arg_name] = self._reduce_args(arg_name, arg_values)

        for arg_name, value in list(resolved_args.items()):
            if not isinstance(value, str):
                continue

            for match in re.finditer(self._variable_template_pattern, value):
                arg_value: Any = None
                if arg_variable := re.search(
                    self._variable_resolved_name_pattern,
                    match.group(0),
                ):
                    arg_value = resolved_args.get(arg_variable.group(0))

                if arg_value is not None:
                    value = re.sub(
                        re.escape(match.group(0)),
                        lambda _: str(arg_value),
                        value,
                    )

            resolved_args[arg_name] = value

        env_values: Dict[str, Any] = {}
        env_layers = self.layers(layer_types='env')
        for layer in env_layers:
            if not isinstance(layer, Env):
                continue

            for key, value in zip(layer.keys, layer.values):
                resolved_val: Any = value
                if isinstance(resolved_val, str):
                    for match in re.finditer(
                        self._variable_template_pattern,
                        resolved_val,
                    ):
                        envar_value: Any = None
                        if envar_variable := re.search(
                            self._variable_resolved_name_pattern,
                            match.group(0),
                        ):
                            envar_value = resolved_args.get(
                                envar_variable.group(0)
                            )

                        if envar_value is not None:
                            resolved_val = re.sub(
                                re.escape(match.group(0)),
                                lambda _: str(envar_value),
                                resolved_val,
                            )

                    if not re.search(
                        self._variable_template_pattern,
                        resolved_val,
                    ):
                        env_values[key] = resolved_val
                else:
                    env_values[key] = resolved_val

        resolved_args.update(env_values)

        for arg_name, value in list(resolved_args.items()):
            if isinstance(value, str):
                resolved_args.update(
                    self._resolve_args(arg_name, value, resolved_args)
                )

        return resolved_args

    def _substitute_variables(
        self,
        text: str,
        resolved_args: Dict[str, Any],
    ) -> str:
        matches: Set[Tuple[str, str]] = set()
        for match in re.finditer(self._variable_template_pattern, text):
            if resolved_name := re.search(
                self._variable_resolved_name_pattern,
                match.group(0),
            ):
                matches.add((resolved_name.group(0), match.group(0)))

        for resolved_name_str, _ in matches:
            resolved_value = resolved_args.get(resolved_name_str)
            if resolved_value is not None:
                escaped = re.escape(resolved_name_str)
                pattern = (
                    r'\$\{'
                    + escaped
                    + r'(?::-[^}]*)?\}|\$'
                    + escaped
                    + r'(?!\w)'
                )
                text = re.sub(pattern, lambda _: str(resolved_value), text)

        return text

    def _resolve_layer(
        self,
        layer: LayerType,
        resolved_args: Dict[str, Any],
    ) -> LayerType:
        model_data = layer.model_dump()
        for field, field_value in model_data.items():
            if isinstance(field_value, str):
                model_data[field] = self._substitute_variables(
                    field_value,
                    resolved_args,
                )
            elif isinstance(field_value, list):
                for idx, value in enumerate(field_value):
                    if isinstance(value, str):
                        model_data[field][idx] = self._substitute_variables(
                            value,
                            resolved_args,
                        )

        return layer.model_copy(update=model_data)

    def _reduce_args(
        self,
        arg_name: str,
        args: Dict[str, Any],
        visited: Optional[Set[str]] = None,
    ) -> Any:
        if visited is None:
            visited = set()
        if arg_name in visited:
            return args.get(arg_name)
        visited.add(arg_name)

        arg_value = args.get(arg_name)
        if isinstance(arg_value, str) and arg_value in args:
            return self._reduce_args(arg_value, args, visited)

        return arg_value

    def _resolve_args(
        self,
        arg_name: str,
        value: Optional[str],
        resolved: Dict[str, Any],
    ) -> Dict[str, Any]:
        if value is None:
            return resolved

        resolved_items = [
            (resolved_name, resolved_value)
            for resolved_name, resolved_value in resolved.items()
            if isinstance(resolved_value, str) and resolved_value != value
        ]

        for resolved_arg, resolved_value in resolved_items:
            updated = resolved_value
            for match in re.finditer(r'(\$)([\w]+)', updated):
                match_key = match.group(2)
                if arg_name == match_key:
                    updated = re.sub(
                        r'\$' + re.escape(match_key) + r'(?!\w)',
                        lambda _: value,
                        updated,
                    )

            for match in re.finditer(r'(\$\{)([\w]+)(\})', updated):
                match_key = match.group(2)
                if arg_name == match_key:
                    updated = updated.replace(match.group(0), value)

            resolved[resolved_arg] = updated

        return resolved

    def to_string(self) -> str:
        return '\n\n'.join(
            [layer.to_string().strip('\n') for layer in self._layers]
        )

    def to_context(self) -> MemoryFile:
        encoded = self.to_string().encode('utf-8')
        image_file = MemoryFile(encoded, name='Dockerfile')
        image_file.seek(0)

        tar_file = MemoryFile(b'', file_number=image_file.file_number + 1)

        with tarfile.open(fileobj=tar_file, mode='w') as context:
            image_file_info = tarfile.TarInfo(name='Dockerfile')
            image_file_info.size = len(encoded)
            context.addfile(image_file_info, image_file)

            seen_arcnames: Set[str] = {'Dockerfile'}
            for file in self.files:
                if not os.path.exists(file):
                    continue
                filename = pathlib.Path(file).name
                if filename in seen_arcnames:
                    continue
                seen_arcnames.add(filename)

                with open(file, 'rb') as context_file:
                    info = context.gettarinfo(
                        fileobj=context_file,
                        arcname=filename,
                    )
                    context.addfile(info, context_file)

        tar_file.seek(0)
        return tar_file

    def to_file(self, filepath: Optional[str] = None) -> None:
        if filepath is None:
            filepath = self.filename
        elif filepath != self.filename:
            self.filename = filepath

        if filepath not in self.files:
            self.files.append(filepath)

        with open(filepath, 'w') as dockerfile:
            dockerfile.write(self.to_string())

    def to_memory_file(self, filepath: Optional[str] = None) -> MemoryFile:
        name = filepath if filepath is not None else self.filename
        content = self.to_string().encode('utf-8')
        memory_file = MemoryFile(content, name=name)
        memory_file.seek(0)
        return memory_file

    def clear(self) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self._layers.clear()
        self.files.clear()

    def add(
        self,
        source: str,
        destination: str,
        user_id: Optional[str] = None,
        group_id: Optional[str] = None,
        permissions: Optional[Union[str, int]] = None,
        checksum: Optional[str] = None,
        link: bool = False,
    ) -> Image:
        parsed_permissions = (
            str(permissions) if permissions is not None else None
        )
        self._layers.append(
            Add(
                source=source,
                destination=destination,
                user_id=user_id,
                group_id=group_id,
                permissions=parsed_permissions,
                checksum=checksum,
                link=link,
            )
        )
        return self

    def arg(
        self,
        name: str,
        default: Optional[Union[str, int, bool, float]] = None,
    ) -> Image:
        self._layers.append(Arg(name=name, default=default))
        return self

    def cmd(
        self,
        command: List[Union[str, int, bool, float]],
    ) -> Image:
        self._layers.append(Cmd(command=command))
        return self

    def copy(
        self,
        source: str,
        destination: str,
        user_id: Optional[str] = None,
        group_id: Optional[str] = None,
        permissions: Optional[Union[str, int]] = None,
        from_source: Optional[str] = None,
        link: bool = False,
    ) -> Image:
        parsed_permissions = (
            str(permissions) if permissions is not None else None
        )
        copy_layer = Copy(
            source=source,
            destination=destination,
            user_id=user_id,
            group_id=group_id,
            permissions=parsed_permissions,
            from_source=from_source,
            link=link,
        )

        self._layers.append(copy_layer)

        if from_source is None:
            source_str = str(copy_layer.source)
            self.files.append(source_str)

        return self

    def entrypoint(self, command: List[str]) -> Image:
        self._layers.append(Entrypoint(command=command))
        return self

    def env(
        self,
        keys: str | List[str],
        values: (
            str
            | int
            | bool
            | float
            | List[str | int | bool | float]
        ),
    ) -> Image:
        key_list: List[str] = [keys] if isinstance(keys, str) else list(keys)
        value_list: List[str | int | bool | float] = (
            list(values) if isinstance(values, list) else [values]
        )

        self._layers.append(
            Env(
                keys=key_list,
                values=value_list,
            )
        )
        return self

    def expose(self, ports: List[Union[int, str]]) -> Image:
        self._layers.append(Expose(ports=ports))
        return self

    def healthcheck(
        self,
        interval: Optional[Union[int, float]],
        timeout: Optional[Union[int, float]],
        start_period: Optional[Union[int, float]],
        retries: Optional[Union[int, float]],
        command: List[Union[str, int, bool, float]],
    ) -> Image:
        self._layers.append(
            Healthcheck(
                interval=interval,
                timeout=timeout,
                start_period=start_period,
                retries=retries,
                command=Cmd(command=command),
            )
        )
        return self

    def label(self, name: str, value: str) -> Image:
        self._layers.append(Label(name=name, value=value))
        return self

    def maintainer(self, author: str) -> Image:
        self._layers.append(Maintainer(author=author))
        return self

    def onbuild(
        self,
        instruction: (
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
        ),
    ) -> Image:
        self._layers.append(OnBuild(instruction=instruction))
        return self

    def run(
        self,
        command: str,
        network: Optional[Literal['default', 'host', 'none']] = None,
        security: Optional[Literal['insecure', 'sandbox']] = None,
        mount: Optional[Dict[str, Any]] = None,
    ) -> Image:
        mount_type: Union[
            BindMount,
            CacheMount,
            SecretMount,
            SSHMount,
            TMPFSMount,
            None,
        ] = None

        if mount:
            mount_type_name = str(mount.get('mount_type', 'bind'))
            factory = self._mount_types.get(mount_type_name)
            if factory is None:
                raise ValueError(f'Unsupported mount type: {mount_type_name!r}')
            mount_type = factory(mount)

        self._layers.append(
            Run(
                command=command,
                mount=mount_type,
                network=network,
                security=security,
            )
        )
        return self

    def shell(
        self,
        executable: str,
        parameters: Optional[List[str | int | float | bool]] = None,
    ) -> Image:
        self._layers.append(
            Shell(
                executable=executable,
                parameters=parameters,
            )
        )
        return self

    def stage(
        self,
        base: str,
        tag: str = 'latest',
        alias: Optional[str] = None,
        platform: Optional[str] = None,
    ) -> Image:
        self._layers.append(
            Stage(
                base=base,
                tag=tag,
                alias=alias,
                platform=platform,
            )
        )
        return self

    def stopsignal(self, signal: Union[str, int]) -> Image:
        self._layers.append(StopSignal(signal=signal))
        return self

    def user(
        self,
        user_id: str,
        group_id: Optional[str] = None,
    ) -> Image:
        self._layers.append(User(user_id=user_id, group_id=group_id))
        return self

    def volume(self, paths: List[str]) -> Image:
        self._layers.append(Volume(paths=paths))
        return self

    def workdir(self, path: str) -> Image:
        self._layers.append(Workdir(path=path))
        return self
