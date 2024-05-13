import requests

def ask_question(question):
  """
  Simulates asking a question using Google search

  Args:
      question: The user's question

  Returns:
      A string containing the top search result for the question
  """
  # Encode the question for safe use in the URL
  encoded_question = requests.utils.quote(question)

  # Prepare the Google custom search API URL (replace with your own API key)
  url = f"https://www.googleapis.com/customsearch/v1?key=AIzaSyBBPv8LSEwgA7QtPRNPkrgke7CmjMWtmCs&cx=94ee607515bb74272&q={encoded_question}"

  # Make the request and get the response
  response = requests.get(url)
  response.raise_for_status()  # Raise an error if request fails

  # Parse the JSON response
  data = response.json()

  # Extract the top search result (modify if you want more results)
  try:
    answer = data["items"][0]["snippet"]
  except (KeyError, IndexError):
    answer = "Sorry, I couldn't find an answer to your question."

  return answer

def main():
  """
  Main function for the program interaction
  """
  while True:
    question = input("Ask me anything (or type 'quit' to exit): ")
    if question.lower() == "quit":
      break

    answer = ask_question(question)
    print(answer)

if __name__ == "__main__":
  main()
