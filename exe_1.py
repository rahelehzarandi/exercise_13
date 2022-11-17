# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not
# . Use the prior prime number exercise as a starting point. For example, a GET request for number 31 is given
# as: http://127.0.0.1:5000/prime_number/31. The response must be in the format of {"Number":31, "isPrime":true}.


from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def primeNum():
    args = request.args
    number1 = int(args.get("number1"))
    if number1>1:
        for i in range(2,number1):
            if (number1 % i) == 0:
                flag="False"
                break
        else:
            flag="True"
    else:
        flag="False"



    response = {
        "number1" : number1,
        "isprime" :flag
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)