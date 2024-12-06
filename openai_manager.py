from openai import OpenAI

class OpenAIManager:
    def __init__(self):
        self.client = OpenAI()
        self.message_list = self.get_system_message()

    def get_openai(self):
        return self.client
    
    def get_system_message(self):
        return [
            {"role": "system", "content": "You are a helpful assistant."},   
        ] 

    def run_openai(self):
        response = self.client.chat.completions.create(
            model = "gpt-4o",
            messages=self.message_list
        )
        return response.choices[0].message.content

# if __name__ == "__main__":

#     manager = OpenAIManager()

#     while True:
#         user_input =input("Mehmet : ")
#         manager.message_list.append({"role": "user", "content": user_input})
#         response = manager.run_openai()
#         assistant_message = response
#         manager.message_list.append({"role": "assistant", "content": assistant_message})
#         print("Assistant : ", assistant_message)
        