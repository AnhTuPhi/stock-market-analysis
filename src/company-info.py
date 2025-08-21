import os.path

from vnstock import Company
from loguru import logger
import json
from typing import Any, Dict

WATCHLIST_FILE = "../data/watchlist.txt"
OUTPUT_DIR = "../data/stock"


def get_list_symbols() -> Any:
    # Read watchlist
    with open(WATCHLIST_FILE, "r", encoding="utf-8") as stream:
        return [line.strip() for line in stream if line.strip()]

def get_company_info(symbol: str) -> Dict[str, Any]:
    logger.info("Fetching company info of {}", symbol)

    try:
        company_info = Company(symbol=symbol, source="VCI")
        overview_df = company_info.overview()

        if overview_df is None:
            logger.warning("No data found for {}", symbol)
            return {}

        return overview_df.to_dict(orient="records")[0]

    except Exception as ex:
        logger.error("Fetching company info of {} got error: {}", symbol, ex)
        return {}

def save_data(symbol: str, company_info: Dict[str, Any]) -> None:
    logger.info("Saving company info of {}", symbol)
    if not company_info:
        return

    stock_dir = os.path.join(OUTPUT_DIR, symbol)
    os.makedirs(stock_dir, exist_ok=True)

    output_file = os.path.join(stock_dir, f"{symbol}.json")
    with open(output_file, "w", encoding="utf-8") as stream:
        json.dump(company_info, stream, ensure_ascii=False, indent=4)

    logger.success("Saved {} info to {}", symbol, output_file)

if __name__ == '__main__':
    logger.info('Start crawling watchlist company info')

    symbols = get_list_symbols()
    logger.info("Found {} symbols in watchlist: {}", len(symbols), symbols)

    for symbol in symbols:
        company_info = get_company_info(symbol)
        save_data(symbol, company_info)
