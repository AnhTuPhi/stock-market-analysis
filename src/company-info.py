import logging
import os.path

from tenacity import sleep
from vnstock import Company
from loguru import logger
import json
from typing import Any, Dict
import time

WATCHLIST_FILE = "../data/watchlist.txt"
OUTPUT_DIR = "../data/stock"


def get_list_symbols() -> Any:
    # Read watchlist
    with open(WATCHLIST_FILE, "r", encoding="utf-8") as stream:
        return [line.strip() for line in stream if line.strip()]

def safe_fetch(fetch_fn, name, symbol, to_records=True, single=False):
    try:
        df = fetch_fn()
        if df is None or df.empty:
            return {} if single else []
        records = df.to_dict(orient="records")
        return records[0] if single else records
    except Exception as e:
        logger.error("{}() failed for {}: {}", name, symbol, e)
        return {} if single else []

def format_subsidiaries(officers: list[dict]) -> list[dict]:
    result = []
    for o in officers:
        o = o.copy()
        if "ownership_percent" in o and isinstance(o["ownership_percent"], (int, float)):
            o["percentage"] = f"{o['ownership_percent'] * 100:.2f}%"
        result.append(o)
    return result

def format_shareholders(officers: list[dict]) -> list[dict]:
    result = []
    for o in officers:
        o = o.copy()
        if "share_own_percent" in o and isinstance(o["share_own_percent"], (int, float)):
            o["percentage"] = f"{o['share_own_percent'] * 100:.2f}%"
        result.append(o)
    return result

def format_affiliates(officers: list[dict]) -> list[dict]:
    result = []
    for o in officers:
        o = o.copy()
        if "ownership_percent" in o and isinstance(o["ownership_percent"], (int, float)):
            o["percentage"] = f"{o['ownership_percent'] * 100:.2f}%"
        result.append(o)
    return result

def format_officers(officers: list[dict]) -> list[dict]:
    result = []
    for o in officers:
        o = o.copy()
        if "officer_own_percent" in o and isinstance(o["officer_own_percent"], (int, float)):
            o["percentage"] = f"{o['officer_own_percent'] * 100:.2f}%"
        result.append(o)
    return result

def get_company_info(symbol: str) -> Dict[str, Any]:
    logger.info("Fetching company info of {}", symbol)

    try:
        company_info = Company(symbol=symbol, source="VCI")
        return {
            "overview": safe_fetch(company_info.overview, "overview", symbol, single=True),
            "shareholders": format_shareholders(
                safe_fetch(company_info.shareholders, "shareholders", symbol)
            ),
            "subsidiaries": format_subsidiaries(
                safe_fetch(company_info.subsidiaries, "subsidiaries", symbol)
            ),
            "affiliates": format_affiliates(
                safe_fetch(company_info.affiliate, "affiliate", symbol)
            ),
            "officers": format_officers(
                safe_fetch(lambda: company_info.officers(filter_by="working").head(),"officers", symbol)
            ),
        }
    except Exception as ex:
        logger.error("Fetching company info of {} got error: {}", symbol, ex)
        return {}


def save_overview_data(symbol: str) -> None:
    logger.info("Saving company info of {}", symbol)

    stock_dir = os.path.join(OUTPUT_DIR, symbol)
    os.makedirs(stock_dir, exist_ok=True)

    output_file = os.path.join(stock_dir, f"{symbol}_OVERVIEW.json")
    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as stream:
            try :
                exist_data = json.load(stream)
            except json.JSONDecodeError:
                exist_data = {}
    else:
        exist_data = {}

    # Update overview
    company_info = get_company_info(symbol)
    exist_data.update(company_info)

    with open(output_file, "w", encoding="utf-8") as stream:
        json.dump(exist_data, stream, ensure_ascii=False, indent=4)

    logger.success("Saved {} info to {}", symbol, output_file)

if __name__ == '__main__':
    logger.info('Start crawling watchlist company info')

    symbols = get_list_symbols()
    logger.info("Found {} symbols in watchlist: {}", len(symbols), symbols)

    for symbol in symbols:
        try:
            save_overview_data(symbol)
        except Exception as e:
            logger.error("Fetch data {} error due to {}", symbol, e)
            time.sleep(15) # Back-off on error, especially rate-limit
        time.sleep(5) # Add delay to reduce rate-limit issues
