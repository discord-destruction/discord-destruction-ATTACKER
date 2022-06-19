from cx_Freeze import Executable, setup

executables = [Executable("main.py")]

setup(
    name="cool app",
    version="1.0.0",
    description="most coolest app ever",
    executables=executables,
)