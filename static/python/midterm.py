from dotenv import load_dotenv
from pint import UnitRegistry
from requests import get
from pathlib import Path
from os import getenv

env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
reg = UnitRegistry()
Q__ = reg.Quantity

API_URL: str = f'https://api.freecurrencyapi.com/v1/latest?apikey={getenv("API_KEY")}'

units: dict[str, list[str]] = {
    'length': ['mm', 'cm', 'm', 'km'],
    'capacity': ['ML', 'L'],
    'temperature': ['celsius' ,'fahrenheit', 'kelvin'],
    'currency': ['USD', 'INR', 'AUD', 'CAD', 'CHF']
}

def calculate(amount: float, unitGroup: str, un1: str, un2: str) -> str:

    try:
        if unitGroup == 'temperature':
            unit_map = {
                'celsius': 'degC',
                'fahrenheit': 'degF',
                'kelvin': 'kelvin'
            }
            q = Q__(amount, unit_map[un1.lower()])
            result = q.to(unit_map[un2.lower()])

        elif unitGroup == 'currency':
            return str(float(get(API_URL + f'&base_currency={un1.upper()}').json()['data'][un2.upper()]) * amount)

        else:
            q = amount * reg(un1)
            result = q.to(un2)

        return f"{result.magnitude:.2f} {result.units}"

    except Exception as e:
        return f"Error: {e}"

print(API_URL)
