from src.llm.prompt_builder import Prompt_Builder

builder = Prompt_Builder ()

profile = {
    "Name":"Inan Biswas",
    "College":"SASTRA Deemed University, Thanjavur, Tamil Nadu",
    "Interest":"Artificial Intelligence & Data Analysis"
}

prompt = builder.build_prompt_function (
    user_message = "Hello !!",
    user_profile = profile,
    emotion = "Happy"
)
print (prompt)