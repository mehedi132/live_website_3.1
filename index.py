from flask import Flask, redirect, url_for, request, render_template



app=Flask(__name__)

@app.route('/', defaults= {'result':"Wrong Input"})
@app.route('/<result>')
def mainpage(result):
    return render_template("index.html", result = result)

@app.route('/submit', methods=['GET'])
def submit():
    
      S1=request.args['input']
      S2=request.args['v1']
      S3=request.args['input2']
      
      if S1=="Meter" and S3=="Inch"and int(S2)>0: 
        r=int(S2)*39.3701
       #print(""+S2)
        return redirect(url_for('mainpage', result=str(r)+" "+S3)) 
      elif S1=="Meter" and S3=="Centimeter"and int(S2)>0:
          r=int(S2)*100
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      elif S1=="Meter" and S3=="Foot"and int(S2)>0:
          r=int(S2)*3.28084
          return redirect(url_for('mainpage', result=str(r)+" "+S3)) 
          
      elif S1=="Centimeter" and S3=="Meter"and int(S2)>0:
          r=int(S2)/100
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      elif S1=="Centimeter" and S3=="Inch"and int(S2)>0:
      
          r=int(S2)*0.393701
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      elif S1=="Centimeter" and S3=="Foot"and int(S2)>0:
          r=int(S2)*0.0328084
          return redirect(url_for('mainpage', result=str(r)+" "+S3))

      elif S1=="Inch" and S3=="Meter"and int(S2)>0:
          r=int(S2)*0.0254
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      elif S1=="Inch" and S3=="Centimeter"and int(S2)>0:
          r=int(S2)*2.54
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      elif S1=="Inch" and S3=="Foot"and int(S2)>0:
          r=int(S2)/12
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      
      elif S1=="Foot" and S3=="Centimeter"and int(S2)>0:
          r=int(S2)*30.48
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      elif S1=="Foot" and S3=="Meter"and int(S2)>0:
          r=int(S2)*0.3048
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      elif S1=="Foot" and S3=="Inch" and int(S2)>0:
          r=int(S2)*12
          return redirect(url_for('mainpage', result=str(r)+" "+S3))
      else:
         return redirect(url_for('mainpage')) 




if __name__ == '__main__':
    app.run(debug=True)
