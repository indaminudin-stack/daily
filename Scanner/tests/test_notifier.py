import sys
import os 
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.notifier import send_telegram

TOKEN = "8698232598:AAENfKnXvBo3tA3Z52IGf1r7Ylnv0cKhShc"
CHAT_ID = "8876505556"

msg = """
📈 *TEST SCANNER IDX*

1. BBRI
2. BMRI
3. BBCA
"""

send_telegram(msg, TOKEN, CHAT_ID)