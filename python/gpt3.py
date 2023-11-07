import openai
openai.api_key = "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"

f = open(r"C:\Users\clown hikka\Desktop\Папки\python\text.txt", "r")
txt_file = f.read()
f.close()
#user_input = str(input(""))

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=txt_file,
    max_tokens=500,
    temperature=0
)

print(response["choices"][0]["text"])