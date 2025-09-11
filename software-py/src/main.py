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
                    lastprice_integer = int(float(ticker['last']) * 100) # multiples price by 100 to get an integer instead of a float with two decimal places
                    vol24h_integer = round(float(ticker['vol24h'])) # rounds 12 digit volume to the nearest whole number to get a six digit integer

                    lpbyte3 = (lastprice_integer >> 24) & 0xFF  # most significant byte of lastprice_integer
                    lpbyte2 = (lastprice_integer >> 16) & 0xFF
                    lpbyte1 = (lastprice_integer >> 8) & 0xFF
                    lpbyte0 = lastprice_integer & 0xFF

                    vhbyte3 = (vol24h_integer >> 24) & 0xFF     # most significant byte of vol24h_integer
                    vhbyte2 = (vol24h_integer >> 16) & 0xFF
                    vhbyte1 = (vol24h_integer >> 8) & 0xFF
                    vhbyte0 = vol24h_integer & 0xFF



                    ### debug prints
                    print(
                        # f"Instrument: {ticker['instId']}, " unnecessary for now
                        f"Last Price: {ticker['last']},     "
                        # f"Best Bid: {ticker['bidPx']},    " simplified for UART
                        # f"Best Ask: {ticker['askPx']},    "
                        f"24h Volume: {ticker['vol24h']},   "
                        f"LPI: {lastprice_integer},         "
                        f"VTI: {vol24h_integer}             "
                    )
             
asyncio.run(main())
