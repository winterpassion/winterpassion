from flask import Flask,render_template,flash,request,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
@app.route('/user')
def mydate():
    return render_template('index.html')


@app.route('/mydata',methods=['GET', 'POST'])
def mydata():
    if request.form.get('text1') == 'winter':
        return redirect('http://city.lkkids.com')

    else:
        return render_template('404.html')
if __name__=='__main__':
    app.run()