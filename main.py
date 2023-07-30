import openai
from textbase.message import Message
from textbase import models
import os
from typing import List

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like. The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a pleasant chat!
"""

def generate_quiz_question():
    # Function to generate a random quiz question using OpenAI's GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a trivia question.",
        max_tokens=100,
        stop="\n"
    )
    question = response['choices'][0]['text'].strip()
    return question

def evaluate_answer(question, user_answer):
    # Function to evaluate the user's answer to the quiz question using OpenAI's GPT-3.5
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Evaluate the answer to the following question:\nQuestion: {question}\nAnswer: {user_answer}\n",
        max_tokens=100,
        stop="\n"
    )
    feedback = response['choices'][0]['text'].strip()
    return feedback

@textbase.chatbot("trivio-bot")
def on_message(message_history: List[Message]):
    """TrivioBot chatbot logic
    message_history: List of user messages

    Return a string with the bot_response
    """

    # Get the latest user message
    user_message = message_history[-1].text

    # Check if user wants to exit the quiz
    if user_message.lower() in ['exit', 'bye', 'quit']:
        return "TrivioBot: Thanks for playing! Goodbye!"

    # Generate a random quiz question
    quiz_question = generate_quiz_question()
    bot_response = f"TrivioBot: Here's your question: {quiz_question}"

    return bot_response

if __name__ == "__main__":
    # You can use this part to test the TrivioBot using the textbase UI
    models.OpenAI.api_key = "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"
    textbase.run("talking-bot")
