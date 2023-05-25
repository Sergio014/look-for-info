import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lookforinfo.settings')
django.setup()


import openai as ai
from page.models import Page
from django.template.defaultfilters import slugify
from lookforinfo.settings import API_KEY


ai.api_key = API_KEY

def generate_gpt3_response(user_text, print_output=False, max_tokens=3500):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    user_text += ". Please can you write a large response?"
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=max_tokens,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text
 
for i in range(0, 100): 
    title = generate_gpt3_response("Ask interesting question, but do not repeat question that you have already asked and do not answer the question, your response must be only one question")

    text = generate_gpt3_response(title).replace("\n", "<br>")

    url_path = slugify(title)
    if Page.objects.filter(url_path=url_path).exists():
        continue

    page = Page.objects.create(title=title, text=text, url_path=url_path)
    page.save()

print("Succesfully added")