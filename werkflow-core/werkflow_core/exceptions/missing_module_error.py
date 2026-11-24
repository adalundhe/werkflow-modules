from werkflow_core.base.module import Module


class MissingModuleError(Exception):

    def __init__(
        self,
        module: Module
    ) -> None:
        module_name = module.__class__.__name__
        dependencies = list(module.dependencies)

        if dependencies:
            dependency_names = '\n\t- '.join(dependencies)
            message = (
                f'Module {module_name} is missing or its dependencies:\n'
                f'\t- {dependency_names}\n'
                f'have not been installed.'
            )
        else:
            message = f'Module {module_name} is missing or its dependencies have not been installed.'

        super().__init__(message)
