from langchain_dartmouth.llms import DartmouthLLM, ChatDartmouth

import os
# os.environ["DARTMOUTH_API_KEY"] = "gytO2vSP77kl6d9GYmvh92fh6mmx4B9xlOU67PfXYRuz6MPCBnh4W1LSI734McymFLLTwfkzRyRdpPHG8vjfB1zEESHZlTyqhqAQUvXqvVMK8iejpvDfjEeZTPB5taS4XuEoRmSCVaV8j0bgEwnZJ1hfNqtNWg46SfEwFyHqQ9Ye5SuzG3rmpmjB5RTfLMkFZDLS9bdGVvqDtGTUQOerS0mLm8swHDIWEzuRvU86MYp64hThJQqSTvmgO7rKV9IROBHDOwsxWPYiMl3QRP6h8G1dvQWAbLUDrnxwRSbpTc4ybwPU1NdphDwM3bMOuEgRO9WESqLZTHOF9gGYCvHMjAyk"

# llm = DartmouthLLM(dartmouth_api_key="gytO2vSP77kl6d9GYmvh92fh6mmx4B9xlOU67PfXYRuz6MPCBnh4W1LSI734McymFLLTwfkzRyRdpPHG8vjfB1zEESHZlTyqhqAQUvXqvVMK8iejpvDfjEeZTPB5taS4XuEoRmSCVaV8j0bgEwnZJ1hfNqtNWg46SfEwFyHqQ9Ye5SuzG3rmpmjB5RTfLMkFZDLS9bdGVvqDtGTUQOerS0mLm8swHDIWEzuRvU86MYp64hThJQqSTvmgO7rKV9IROBHDOwsxWPYiMl3QRP6h8G1dvQWAbLUDrnxwRSbpTc4ybwPU1NdphDwM3bMOuEgRO9WESqLZTHOF9gGYCvHMjAyk")

# chat_model = ChatDartmouth(dartmouth_chat_api_key="sk-4394f7e9a178428e8d6245158291d6d9")


# Import libraries
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from langchain_dartmouth.llms import ChatDartmouth
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Set the environment variable for the Dartmouth Chat API key
os.environ["DARTMOUTH_CHAT_API_KEY"] = "sk-4394f7e9a178428e8d6245158291d6d9"

# Input unstructured text
UNSTRUCTURED_TEXT = """The original, historic library building is the Fisher Ames Baker Memorial Library; it opened in 1928 with a collection of 240,000 volumes. The building was designed by Jens Fredrick Larson, modeled after Independence Hall in Philadelphia, and funded by a gift to Dartmouth College by George Fisher Baker in memory of his uncle, Fisher Ames Baker, Dartmouth class of 1859. The facility was expanded in 1941 and 1957–1958 and received its one millionth volume in 1970.

In 1992, John Berry and the Baker family donated US $30 million for the construction of a new facility, the Berry Library designed by architect Robert Venturi, adjoining the Baker Library. The new complex, the Baker-Berry Library, opened in 2000 and was completed in 2002.[6] The Dartmouth College libraries presently hold over 2 million volumes in their collections."""

# Step 1: Setup prompt template
prompt = PromptTemplate(
    template=(
        "Extract a succinct timeline of events directly related to the Library from the following text. "
        "Return the timeline as a list of dictionaries, where each dictionary has two keys: 'year' and 'event'. "
        "Format your output in JSON format. The text: \n\n{unstructured_text}"
    )
)

# Step 2: Initialize Dartmouth Chat LLM
llm = ChatDartmouth(model_name="meta.llama-3.2-11b-vision-instruct")

# Step 3: Setup JSON output parser
parser = JsonOutputParser()

# Step 4: Sequentially invoke components
formatted_prompt = prompt.invoke({"unstructured_text": UNSTRUCTURED_TEXT})
llm_response = llm.invoke(formatted_prompt)
timeline = parser.invoke(llm_response)

# Step 5: Print extracted timeline
print("Timeline of events:")
for event in timeline:
    print(event)

# Step 6: Using chain composition with | operator
timeline_extraction_chain = prompt | llm | parser
# Invoke chain in a single call
timeline_chain_result = timeline_extraction_chain.invoke({"unstructured_text": UNSTRUCTURED_TEXT})

print("\nTimeline using chain:")
for event in timeline_chain_result:
    print(event)


git rm -r --cached .
git add .
git commit -m "Apply .gitignore and remove ignored files"