import decimal
name = "Fred"
f"He said his name is {name}."

width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"result: {value:{width}.{precision}}"  # nested fields


'{:_}'.format(1000000)

'{:_x}'.format(0xFFFFFFFF)
