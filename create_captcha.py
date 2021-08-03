#generate image captcha
from captcha.image import ImageCaptcha
image = ImageCaptcha()

image_data = image.generate('amith')
image.write('amith', 'captcha.png')

#generate audio captcha
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
audio_data = audio.generate('1111')
audio.write('1111', 'audio.wav')
