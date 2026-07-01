from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    client = get_client()

    try:
        logger.info(
            f"MARKET ORDER REQUEST: symbol={symbol}, side={side}, quantity={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(
            f"MARKET ORDER RESPONSE: {response}"
        )

        return response

    except Exception as e:
        logger.error(f"MARKET ORDER ERROR: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        logger.info(
            f"LIMIT ORDER REQUEST: symbol={symbol}, side={side}, quantity={quantity}, price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(
            f"LIMIT ORDER RESPONSE: {response}"
        )

        return response

    except Exception as e:
        logger.error(f"LIMIT ORDER ERROR: {str(e)}")
        raise