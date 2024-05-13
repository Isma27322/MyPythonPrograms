i = 1
quotesfixed = []
with open('quotes.txt', 'r') as quotes_file:
    for line in quotes_file:
        remove1 = line.strip()
        remove2 = remove1.strip("\\")
        remove3 = remove2.strip(f"{i}.")
        quotesfixed.append(remove3)
        i += 1


with open('quotes_fixed.txt', 'w') as fixed_quotes:
    for quote in quotesfixed:
        fixed_quotes.write(f"{quote}\n")


print('The quotes should now be written to "quotes_fixed.txt".')
