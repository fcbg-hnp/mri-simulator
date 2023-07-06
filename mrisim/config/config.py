from __future__ import annotations  # c.f. PEP 563, PEP 649

from configparser import ConfigParser
from typing import TYPE_CHECKING

from ..utils._checks import ensure_path
from ..utils._docs import fill_doc

if TYPE_CHECKING:
    from pathlib import Path
    from typing import Optional, Tuple, Union


@fill_doc
def read_config(
    fname: Optional[Union[str, Path]] = None
) -> Tuple[str, int, float, float]:
    """Read a ``.ini`` configuration file.

    Parameters
    ----------
    fname : path-like
        Path to the ``.ini`` configuration containing a single ``'params'``
        section with 4 keys: ``'key'``, ``'period'``, ``'repetition'``,
        ``'wait'``.

    Returns
    -------
    %(key)s
    %(repetition)s
    %(period)s
    %(wait)s
    """
    fname = ensure_path(fname, must_exist=True)
    config = ConfigParser(inline_comment_prefixes=("#", ";"))
    config.optionxform = str
    config.read(str(fname))

    if not config.has_section("params"):
        raise ValueError(
            "The configuration file should have a single 'params' section."
        )
    if sorted(config["params"].keys()) != [
        "key",
        "period",
        "repetition",
        "wait",
    ]:
        raise ValueError(
            "The configuration file section 'params' should have 4 keys: "
            "'key', 'period', 'repetition', 'wait'."
        )

    # extract variables
    key = config["params"]["key"]
    repetition = int(config["params"]["repetition"])
    period = int(config["params"]["period"]) / 1000
    wait = int(config["params"]["wait"]) / 1000

    if repetition <= 0:
        raise ValueError(
            "The number of repetition should be a strictly positive integer. "
            f"{repetition} is invalid."
        )
    if period < 0:
        raise ValueError(
            f"The period should be a positive number. {period} is invalid."
        )
    if wait < 0:
        raise ValueError(f"The wait should be a positive number. {wait} is invalid.")

    return key, repetition, period, wait
