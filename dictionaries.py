# We use dictionaries to store data in a more complete way than lists, using a key and a value
# In this case, we are going to set a dictionary which the key represents who we are talking about and the value is a grade to their importance in today's world for a tech entrepreneur perspective.
power_rankings = {
    "Nvidia": 10,  # Nvidia is the key and the value is 10. And so goes up to the end of the dictionary.
    "Trump": 10,
    "China": 10,
    "War": 10,
    "AI Regulation": 10,
    "OpenAI": 9.5,
    "Anthropic": 9.5,
    "Google": 9.5,
    "Federal Reserve": 9,
    "Oil": 9,
    "Stocks": 8.5,
    "Markets": 8,
}


power_score = power_rankings["Federal Reserve"]   # Goes into the "power_rankings" dictionaries, and asks what is the value for the key "Federal Reserve", and stores that into the "power_score" variable.
power_score_two = power_rankings["Trump"]   # Does the same process as the last one, but now for the key "Trump", and stores it the "power_score_two" variable.
print(f"The power score for the Federal Reserve is {power_score}.")   # Prints into the terminal the power score for "Federal Reserve"
print(f"The power score for Donald Trump is {power_score_two}.")   # Prints into the terminal the power score for "Trump"
print(f"{power_rankings}")   # Prints the entire dictionary, its keys and values.