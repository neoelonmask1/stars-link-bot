import logging

logger = logging.getLogger(__name__)


def parse_refund_command(text: str) -> tuple[int | None, str | None]:
    """
    Parse refund command: /refund <user_id> [transaction_id]

    Returns:
        Tuple of (user_id, transaction_id) or (None, None) if invalid format.
    """
    parts: list[str] = text.split()

    if len(parts) < 2 or len(parts) > 3:
        return None, None

    try:
        user_id: int = int(parts[1])
    except ValueError:
        return None, None

    transaction_id: str | None = parts[2] if len(parts) == 3 else None
    return user_id, transaction_id


def extract_user_id(tx: object) -> int | None:
    """Extract payer user_id from transaction.source.user.id."""
    user_id = getattr(getattr(getattr(tx, "source", None), "user", None), "id", None)
    if isinstance(user_id, int):
        return user_id

    logger.debug(f"Unable to extract user_id from transaction {tx} source.user.id")
    return None


def extract_charge_id(tx: object) -> str | None:
    """Extract charge ID from transaction.id."""
    charge_id = getattr(tx, "id", None)
    if isinstance(charge_id, str) and charge_id:
        return charge_id

    logger.debug(f"Unable to extract charge_id from transaction {tx}")
    return None
