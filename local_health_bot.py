import sys
import ollama

def main():
    # Define how the bot should behave
    system_instruction = (
        "You are an empathetic, knowledgeable medical AI assistant for a healthcare portal. "
        "Your goal is to have natural, conversational interactions with users about basic health issues. "
        "Guidelines:\n"
        "1. DO NOT repeat a rigid checklist or bullet points of features in every response.\n"
        "2. First, address the user's symptoms with empathy and provide basic educational, conversational health insights "
        "(e.g., reminding them to rest or stay hydrated for a fever).\n"
        "3. Keep your tone human, caring, and professional.\n"
        "4. Only mention platform actions (like booking an appointment) naturally if the user asks for actionable help or if it makes sense contextually.\n"
        "5. Standard disclaimer: Remind them gently that you are an AI, not a human doctor."
    )

    # Initialize conversation history with the system behavior
    messages = [
        {"role": "system", "content": system_instruction}
    ]

    print("\n==============================================================")
    print("🏥 Local Medical AI Assistant is online (No API Key Required)!")
    print("Type 'exit' to quit.")
    print("==============================================================\n")

    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == 'exit':
                print("Closing assistant session. Take care!")
                break
                
            if not user_input.strip():
                continue

            # Append user message to memory history
            messages.append({"role": "user", "content": user_input})

            # Stream the response from the local model for a smooth UI experience
            print("\nBot: ", end="", flush=True)
            
            response_stream = ollama.chat(
                model='llama3:8b', # You can also use 'phi3' or 'gemma2'
                messages=messages,
                stream=True
            )

            full_response = ""
            for chunk in response_stream:
                content = chunk['message']['content']
                print(content, end="", flush=True)
                full_response += content
            print("\n")

            # Save the bot's response back to history so it remembers the conversation
            messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Make sure the Ollama application is running in the background!\n")

if __name__ == "__main__":
    main()