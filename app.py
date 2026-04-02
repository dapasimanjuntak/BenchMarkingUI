from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def loan_step1():
    return render_template('loan/loan_step1.html')

@app.route('/loanAgreement/step2')
def loan_step2():
    return render_template('loan/loan_step2.html')

@app.route('/loanAgreement/step3')
def loan_step3():
    return render_template('loan/loan_step3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)