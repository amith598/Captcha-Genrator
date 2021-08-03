#generate image captcha
from captcha.image import ImageCaptcha
from random import randint
poll = randint(999, 9999)
image = ImageCaptcha()

image_data = image.generate(poll)
image.write(poll, 'captcha.png')

#generate audio captcha
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
audio_data = audio.generate('1111')
audio.write('1111', 'audio.wav')
