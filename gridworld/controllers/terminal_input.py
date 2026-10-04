class TerminalInput:
    """To implement — S0-04. Input source following the InputSource Protocol."""

    def read_key(self) -> str | None:
        """Use input() followed by Enter; return :quit on EOF or interruption."""
        raise NotImplementedError("S0-04: read a command from the terminal")
