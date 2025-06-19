"""Reference portfolio allocations for a pension fund's life cycle.

This module provides simple asset allocation examples for three stages of
a pension fund: growth, maturity, and decline.  The numbers are purely for
illustration and not intended as investment advice.
"""
from dataclasses import dataclass
from typing import Dict


@dataclass
class Portfolio:
    equities: float
    private_equity: float
    real_assets: float
    bonds: float
    cash: float = 0.0

    def as_percentages(self) -> Dict[str, float]:
        """Return the allocation as a dictionary of percentages."""
        return {
            "equities": self.equities * 100,
            "private_equity": self.private_equity * 100,
            "real_assets": self.real_assets * 100,
            "bonds": self.bonds * 100,
            "cash": self.cash * 100,
        }


def reference_portfolio(stage: str) -> Portfolio:
    """Return a reference portfolio allocation for the given life cycle stage.

    Parameters
    ----------
    stage : str
        One of ``"growth"``, ``"maturity"``, or ``"decline"``.

    Returns
    -------
    Portfolio
        Allocation percentages for the requested stage.
    """
    stage = stage.lower()
    if stage == "growth":
        return Portfolio(
            equities=0.6,
            private_equity=0.15,
            real_assets=0.15,
            bonds=0.1,
        )
    if stage == "maturity":
        return Portfolio(
            equities=0.4,
            private_equity=0.1,
            real_assets=0.15,
            bonds=0.35,
        )
    if stage == "decline":
        return Portfolio(
            equities=0.2,
            private_equity=0.0,
            real_assets=0.1,
            bonds=0.6,
            cash=0.1,
        )
    raise ValueError(
        f"Unknown stage: {stage}. Use 'growth', 'maturity', or 'decline'."
    )


def demo() -> None:
    """Print example allocations for each life cycle stage."""
    for phase in ("growth", "maturity", "decline"):
        portfolio = reference_portfolio(phase)
        print(f"{phase.title()} Phase Allocation (%)")
        for name, percent in portfolio.as_percentages().items():
            print(f"  {name:14s}: {percent:5.1f}")
        print()


if __name__ == "__main__":
    demo()
