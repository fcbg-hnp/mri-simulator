# postponed evaluation of annotations, c.f. PEP 563 and PEP 649
# alternatively, the type hints can be defined as strings which will be
# evaluated with eval() prior to type checking.
from __future__ import annotations

from time import sleep
from typing import TYPE_CHECKING

from keyboard import press_and_release

from .utils._docs import fill_doc
from .utils.logs import logger, set_log_level

if TYPE_CHECKING:
    from typing import Optional, Union


@fill_doc
def simulate(
    key: str,
    repetition: int,
    period: float,
    wait: float,
    *,
    verbose: Optional[Union[bool, str, int]] = None,
) -> None:
    """Simulate key-pressed by the MRI.

    Parameters
    ----------
    %(key)s
    %(repetition)s
    %(period)s
    %(wait)s
    %(verbose)s
    """
    if verbose is not None:
        set_log_level(verbose)

    # waiting period before start
    if wait != 0:
        logger.info("Starting waiting mode for %.1f seconds.", wait)
    if wait <= 5:
        sleep(wait)
        logger.info("Finished waiting for %.1f seconds.", wait)
    else:
        total_time = 0
        while total_time < wait:
            sleep(5)
            total_time += 5
            if total_time <= wait:
                logger.info(
                    "In waiting mode for %.1f / %.1f seconds.",
                    total_time,
                    wait,
                )

    # main loop
    logger.info("Starting the MRI simulation.")
    for k in range(repetition):
        press_and_release(key)
        sleep(period)
