import requests
import random

def get_random_quote():
  """Fetches a random quote from an API and returns it as a dictionary"""
  url = "https://api.quotable.io/random"
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Failed to get quote. Status code: {response.status_code}")
    return None

def main():
  """Gets a random quote, shuffles it with potentially existing quotes, and prints one"""
  quotes = []  # List to store retrieved quotes
  while True:
    quote = get_random_quote()
    if quote is None:
      break  # Stop if failed to get a quote
    if quote not in quotes:  # Check if quote is new
      quotes.append(quote)
    random.shuffle(quotes)  # Shuffle quotes for random order
    #print(f"\"{quotes[0]['content']}\" - {quotes[0]['author']}")
    requests.post("https://ntfy.sh/isma2732isaacquotes",
    data= "This is the quote of the day!\n "f"\"{quotes[0]['content']}\" \n It was said by: {quotes[0]['author']}",
    headers={
        "Title": "Quote of the day",
        "Priority": "default",
        "Tags": "tada,speech_balloon"
    })
    break  # Print only one random quote and exit

if __name__ == "__main__":
  main()
