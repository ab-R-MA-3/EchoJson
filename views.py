from flask import Flask,Blueprint,jsonify,request,Response
import json

# Blueprintのオブジェクトを生成する
app = Blueprint('func', __name__)

#標準 全件取得
@app.route('/api/<resurce>')
def resurce_all(resurce):
    
    #jsonファイルを取得
    if resurce == None:

        try:
            json_file = open('files/err.json','r',encoding='utf-8')
        
        except OSError as e:
            json_load = {"error":"OSError"}

        except FileNotFoundError as e:
            json_load = {"error":"OSError"}

        else:
            json_load = json.load(json_file)
            json_file.close

    else:

        try:
            json_file = open('files/' + resurce + '.json','r',encoding='utf-8')

        except OSError as e:
            json_load = {"error":"OSError"}

        except FileNotFoundError as e:
            json_load = {"error":"OSError"}

        else:
            json_load = json.load(json_file)
            json_file.close

    return jsonify(json_load)
