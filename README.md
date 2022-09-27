# Creating & Coding the Squeeze Indicator in Python

The Squeeze Indicator is a volatility-momentum technical oscillator created by John Carter to measure and trade breakouts. It uses multiple indicators fused together to deliver the buy and sell signals.

## Steps taken to create the indicator:
-  Step 1: Calculate the Bollinger Bands on the market price.
- Step 2: Calculate the Keltner Channel on the market price.
- Step 3: Calculate the highest high in the last 20 periods.
- Step 4: Calculate the lowest low in the last 20 periods.
- Step 5: Find the mean between the two above results.
- Step 6: Calculate a 20-period simple moving average on the closing price
- Step 7: Calculate the delta between the closing price and the mean between the result from step 5 and step 6.
 