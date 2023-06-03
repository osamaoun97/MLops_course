from fastapi import FastAPI
from multiply import multiply
from model import mult_item
import logging

logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger(__name__)

app = FastAPI(debug=True)

@app.get("/")
def home():
    return "hello world"

@app.post("/multiply{a}&{b}")
async def post_multiply(item: mult_item):
    item_dict = item.dict()
    logger.info(f"a = {item_dict['a']}, b = {item_dict['b']}")
    logger.warning("Watch out!")
    return multiply(item_dict["a"],item_dict["b"])