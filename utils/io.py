from typing import Protocol


class Output(Protocol):
    def write(self, message: str) -> None:
        ...


class Input(Protocol):
    def read(self, prompt: str) -> str:
        ...


class ConsoleOutput:
    def write(self, message: str) -> None:
        print(message)  # noqa: WPS421


class ConsoleInput:
    def read(self, prompt: str) -> str:
        return input(prompt)  # noqa: WPS421
