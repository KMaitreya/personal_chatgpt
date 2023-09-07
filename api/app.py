#importing required libraries
import os
import sys
import api.keys as keys
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import GoogleDriveLoader
from langchain.indexes import VectorstoreIndexCreator
from flask import Flask, render_template, request

app=Flask(__name__)

UPLOAD_FOLDER="uploads"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

if __name__=="__main__":
    app.run(debug=True)

@app.route("/")
def index():
    #attaching my openai api key
    return render_template('index.html')

@app.route('/query1', methods=['POST'])
def query1():
    # import pdb
    # pdb.set_trace()
    query=request.form['text']
    os.environ["OPENAI_API_KEY"]=keys.apikey
    Loader=TextLoader('uploads/test.txt')
    # Loader=file_obj
    index=VectorstoreIndexCreator().from_loaders([Loader])
    f=open("uploads/test.txt", 'r')
    return render_template('index.html', op=index.query(query, llm=ChatOpenAI()), fileop=f.read())

@app.route('/upload', methods=['POST'])
def upload():
    # import pdb
    # pdb.set_trace()
    file=request.files['file']
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], "test.txt"))
    f=open("uploads/test.txt", 'r')
    return render_template('index.html', fileop=f.read())

