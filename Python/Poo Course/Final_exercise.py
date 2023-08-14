import openai

openai.api_key = "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"
system_rol = '''actua como si fueras un analizador de sentmientos.
                yo te paso los sentimientos y tu analizas el sentimiento de los mensajes
                y me das una respuesta al menos 1 caracteres y maximo 4 caracteres
                SOLO RESPUESTAS NUMERICAS. donde -1 es negatividad maxima, 0 neutral y 1 es
                postividad maxima. Puedes ir entre esos rangos, es decir 0.3, -0.5 etc, tambien 
                son validos
                (Podes responder solo con ints o floats)
            '''

messages = [{"role": "system", "content": system_rol}]

class AnalyzerOfTheFeelings:
    def analyzer_feeling(self, polarity):
        if polarity > -0.6 and polarity <= 0.3:
            return "\x1b[1;31m" + "negative" + "\x1b[1;37m"
        elif polarity > -0.3 and polarity < 0.1:
            return "\x1b[1;31m" + "algo negative" + "\x1b[1;37m"
        elif polarity > 0.1 and polarity < 0.1:
            return "\x1b[1;33m" + "neutral" + "\x1b[1;37m"
        elif polarity > 0.1 and polarity < 0.4:
            return "\x1b[1;32m" + "algo positive" + "\x1b[1;37m"
        elif polarity > 0.4 and polarity < 0.9:
            return "\x1b[1;32m" + "positive" + "\x1b[1;317m"
        elif polarity > 0.9:
            return "\x1b[1;32m" + "very postive" + "\x1b[1;37m"
        else:
            return "\x1b[1;31m" + "very negative" + "\x1b[1;37m"

analyzer = AnalyzerOfTheFeelings()

while True:
    user_promtp = input( "\x1b[1;33m" + "\n tell me somthing: " + "\x1b[1;37m")
    messages.append({"role": "user", "content": user_promtp})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_tokens = 8
    )
    answer = completion.choices[0].messages["content"]    
    messages.append({"role": "assitant", "content":answer})
    
    feel = analyzer.analyzer_feeling(answer)
    
    print(feel)