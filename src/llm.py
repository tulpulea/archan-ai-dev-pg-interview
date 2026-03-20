def create_llm_wrapper(client, model):
    def llm_wrapper(prompt):
        return client.models.generate_content(model = model, contents=prompt).text
    return llm_wrapper