# DEBUG CODE FOR WEBSOCKET CONNECTION

import websockets 
import asyncio
import json

async def main():
    url = "wss://ws.okx.com:8443/ws/v5/public"
    async with websockets.connect(url) as ws:
        subscribe_message = {
            "op": "subscribe",
            "args": [
                # {"channel": "trades", "instId": "ETH-USDT"} 
                {"channel": "tickers", "instId": "ETH-USDT"}
                ]
        }
        await ws.send(json.dumps(subscribe_message))
        print("Successfully connected to OKX ETH-USDT tickers!") # confirms connection to public OKX API

        while True:
            message = await ws.recv()
            data = json.loads(message)

            if "data" in data: # serialization
                for ticker in data["data"]:

                    ### debug prints
                    print(
                        f"Instrument: {ticker['instId']},   " 
                        f"Last Price: {ticker['last']},     "
                        f"Best Bid: {ticker['bidPx']},      " 
                        f"Best Ask: {ticker['askPx']},      "
                        f"24h Volume: {ticker['vol24h']}    "
                    )
             
asyncio.run(main())
