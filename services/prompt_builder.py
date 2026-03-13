def build_prompt(question, context):

    context_text = "\n".join(context)

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the information provided in the context.

Context: 
{context_text}

Question:
{question}

Answer:
"""

    return prompt
