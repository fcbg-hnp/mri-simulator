from __future__ import annotations  # c.f. PEP 563, PEP 649

from typing import TYPE_CHECKING

from keyboard import press_and_release
from psychopy.clock import wait

from .utils._checks import check_type, ensure_int
from .utils._docs import fill_doc
from .utils.logs import logger, verbose

if TYPE_CHECKING:
    from typing import Optional, Union


@fill_doc
@verbose
def simulate(
    key: str,
    repetition: int,
    period: float,
    wait_start: float = 0,
    *,
    verbose: Optional[Union[bool, str, int]] = None,
) -> None:
    """Simulate key-pressed by the MRI.

    Parameters
    ----------
    %(key)s
    %(repetition)s
    %(period)s
    %(wait_start)s
    %(verbose)s
    """
    check_type(key, (str,), "key")
    repetition = ensure_int(repetition, "repetition")
    check_type(period, ("numeric",), "period")
    check_type(wait_start, ("numeric",), "wait_start")
    if period <= 0:
        raise ValueError("The period must be a strictly positive number.")
    if wait_start < 0:
        raise ValueError("The wait_start duration must be a positive number.")

    # waiting period before start
    if wait_start != 0:
        logger.info("Starting waiting mode for %.1f seconds.", wait_start)
    for k in range(0, wait_start, 5):
        wait_time = 5 if k + 5 < wait_start else wait_start - k
        wait(wait_time, hogCPUperiod=0.2)
        logger.info(
            "In waiting mode for %.1f / %.1f seconds", k + wait_time, wait_start
        )

    # main loop
    logger.info("Starting the MRI simulation.")
    for k in range(repetition):
        press_and_release(key)
        wait(period, hogCPUperiod=0.2)
