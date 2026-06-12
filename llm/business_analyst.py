from llm.groq_client import client


def generate_business_answer(
    question,
    context,
    data
):

    prompt = f"""
    You are a Senior Business Intelligence Analyst.

    Question:
    {question}

    Business Data:
    {data}

    Knowledge Base:
    {context}

    Instructions:

    1. Answer professionally.
    2. Format numbers properly.
    3. Use bullet points when helpful.
    4. Give executive-level insights.
    5. Do not repeat raw tables.
    6. Keep the response under 150 words.
    7. Use markdown formatting.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (
        response
        .choices[0]
        .message
        .content
    )