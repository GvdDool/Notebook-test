# Asking the same question to chatCPT:
def chatGPTrequest(chat_prompt):
  engine="gpt-3.5-turbo" #"text-davinci-002"
  retries = 3

  while retries > 0:
      try:
        #print("test1")

        completion = openai.ChatCompletion.create(
            model=engine,
            messages = [chat_prompt],
            temperature=0.0,
            max_tokens=256,
            request_timeout=30, #increased with 15
            top_p=0.1,
            frequency_penalty=0.1,
            presence_penalty=0.1,
            stop=None
        )

        #print("test2")


        #print(completion['choices'][0]['message']['content'])
        generated_text = completion['choices'][0]['message']['content']

        #print("test3")

        return generated_text

      except Exception as e:
        if e:
            print(e)
            print('Timeout error, retrying...')
            retries -= 1
            wait_time(5)
        else:
            raise e

        print('API is not responding, moving on...')
        bad_api = "x"
        return bad_api

#Testing
boo_test = False
boo_test = True
if boo_test:
  const_prompt = "Give me ten interview questions for the role of project manager"
  #const_prompt = const_prompt1
  chat_prompt = {'role': 'system', 'content': f'{const_prompt}'}


  print("Input: ", chat_prompt)

  test = chatGPTrequest(chat_prompt)
  print(test)


