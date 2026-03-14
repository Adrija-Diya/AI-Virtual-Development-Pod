import google.generativeai as genai

# Requirement Analysis Agent
def requirement_agent(user_task, model):

    prompt = f"""
    You are a software architect.

    Analyze the following development request and break it into clear development steps.

    Request:
    {user_task}

    Provide step-by-step tasks for a developer.
    """

    response = model.generate_content(prompt)

    return response.text


# Code Generation Agent
def code_agent(requirements, model):

    prompt = f"""
    You are a senior software developer.

    Based on the following development steps, generate the code.

    Steps:
    {requirements}

    Provide clean and well-structured code with explanation.
    """

    response = model.generate_content(prompt)

    return response.text

def testing_agent(code, model):

    prompt = f"""
    You are a senior software testing engineer.

    Review the following code and check for:
    - bugs
    - security issues
    - missing validations
    - improvements

    Provide suggestions for improvement.

    Code:
    {code}
    """

    response = model.generate_content(prompt)

    return response.text