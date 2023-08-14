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

class Feeling:
    def __init__(self, name, color):
        self.name = name 
        self.color = color 
        
    def __str__(self):
        return "\x1b[1;{}m{}" + "negative" + "\x1b[1;37m".format(self.color, self.name)

class AnalyzerOfTheFeelings:
    def __init__(self, ranges):
        self.range = ranges
    
    def analyzer_feeling(self, polarity):
        for rango, feel in self.ranges:
            if ranges[0] < polarity <= ranges[1]:
                return feel
        return Feeling("very negative", "31")
    
ranges = [
    ((-0.6 , -0,3)), Feeling("negative","31"),
    ((-0.3 ,-0,1)), Feeling("negative","31"),
    ((-0.1 , -0,1)), Feeling("negative","31"),
    ((0.1 , 0,4)), Feeling("negative","31"),
    ((0.4 , 0,9)), Feeling("negative","31"),
    ((0.9 , 1)), Feeling("negative","31"),
]

analyzer = AnalyzerOfTheFeelings(ranges)

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