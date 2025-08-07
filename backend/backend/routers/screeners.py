from fastapi import APIRouter, Query
from services.screener import find_bullish_stocks

router = APIRouter()

@router.get("/bullish")
def get_bullish(tickers: list[str] = Query(...)):
    return {"bullish": find_bullish_stocks(tickers)}