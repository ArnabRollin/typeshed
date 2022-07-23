import sys
from typing import Any

from ..cmd import Command

if sys.platform == "win32":
    from msilib import Dialog

    class PyDialog(Dialog):
        def __init__(self, *args, **kw) -> None: ...
        def title(self, title) -> None: ...
        def back(self, title, next, name: str = ..., active: int = ...): ...
        def cancel(self, title, next, name: str = ..., active: int = ...): ...
        def next(self, title, next, name: str = ..., active: int = ...): ...
        def xbutton(self, name, title, next, xpos): ...

    class bdist_msi(Command):
        description: str
        user_options: Any
        boolean_options: Any
        all_versions: Any
        other_version: str
        if sys.version_info >= (3, 9):
            def __init__(self, *args, **kw) -> None: ...
        bdist_dir: Any
        plat_name: Any
        keep_temp: int
        no_target_compile: int
        no_target_optimize: int
        target_version: Any
        dist_dir: Any
        skip_build: Any
        install_script: Any
        pre_install_script: Any
        versions: Any
        def initialize_options(self) -> None: ...
        install_script_key: Any
        def finalize_options(self) -> None: ...
        db: Any
        def run(self) -> None: ...
        def add_files(self) -> None: ...
        def add_find_python(self) -> None: ...
        def add_scripts(self) -> None: ...
        def add_ui(self) -> None: ...
        def get_installer_filename(self, fullname): ...