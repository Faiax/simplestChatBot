from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ["hi %1. how are you?"]],
    ['hi i am (.*)', ['hi %1, i am a simplistic chatbot ']],
    ['hello', ['Hi, I am a simplistic chat bot created by Faiaz']],
    ['what can you do', ["I am learning the art of shitting properly"]],
    ['are you stupid', ['Yes, i am stupid. so what? ']],
    ['who are you', ['I am a bot']],
    ['what type of bot are you', ['I am a simplistic chat bot created by Faiaz']],
    ['you are really stupid', ['Good. I appreciate that.']],
    ['who created you', ['I was created by Faiaz']],
    ['What is your name', ['I have no name cause i am a  neglected project']]
]

chat = Chat(pairs, reflections)
chat.converse()
