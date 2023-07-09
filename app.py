"""
Image Caption Generation App
Author: yamesar04
"""

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from GenerateCaptions import predict_step
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('upload.html')
	
@app.route('/', methods = ['GET', 'POST'])
def process():
   if request.method == 'POST':
      img = request.files['image']
      n_captions= int(request.form['num_captions'])
      img_path= f"./static/Images/{img.filename}"
      img.save(img_path)
      kwargs = {"max_length": 16, "num_beams": n_captions, "num_return_sequences":n_captions}
      out= predict_step(image_paths= [img_path], **kwargs)
      return render_template('displayCaptions.html', captions= out, img= img.filename)
		
if __name__ == '__main__':
   app.run(debug = True, port= 8000)