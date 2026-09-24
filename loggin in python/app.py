import logging


## Loggin settings
logging.basicConfig(
    level = logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b;
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result = a-b;
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result


def multiply(a,b):
    result = a*b;
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Attemplted to divide by zero")
        return None

add(10,15)
subtract(10,5)
multiply(10,15)
divide(10,0)