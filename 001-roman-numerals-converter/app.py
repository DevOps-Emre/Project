from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global num
        num = request.form ["number"]
        if num.isdigit() :
            num = int(num)
            if (num >=1) and (num < 4000):
                number_decimal = num
                number_roman = convert(num)
                return render_template("result.html", developer_name = "E2450-Ozan", number_decimal = number_decimal, number_roman = number_roman)
            else:
                return render_template("index.html", developer_name = "E2450-Ozan", not_valid= True)
        else:
            return render_template("index.html", developer_name = "E2450-Ozan", not_valid= True)
    else:
        return render_template("index.html", developer_name = "E2450-Ozan")


def convert(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    number_roman = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            number_roman += syb[i]
            num -= val[i]
        i += 1
    return (number_roman)
 
if __name__ == '__main__':
    app.run(debug = True)
   #app.run(host='0.0.0.0', port=80) 

