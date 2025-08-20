from flask import Flask, render_template_string, request
from base_changer import convert_base

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Base Converter</title>
    <style>
        body {
            padding: 40px;
            font-size: 1.3em;
            font-family: 'Segoe UI', Arial, sans-serif;
            position: relative;
            min-height: 100vh;
            margin: 0;
        }
        .bg-abacus {
            position: fixed;
            top: 50%;
            left: 50%;
            width: 100vw;
            height: 100vh;
            transform: translate(-50%, -50%);
            z-index: 0;
            opacity: 0.08;
            background: url('https://www.svgrepo.com/show/108785/abacus.svg') no-repeat center center;
            background-size: contain;
            pointer-events: none;
        }
        .content {
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        h2 {
            font-size: 2.8em;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 32px;
            color: #333;
        }
        form {
            margin-bottom: 30px;
        }
        form label {
            font-weight: 500;
            font-size: 1.1em;
            margin-bottom: 8px;
            background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            display: block;
        }
        form input {
            margin-bottom: 14px;
            display: block;
        }
        .result {
            font-size: 2em;
            font-weight: bold;
            color: purple;
        }
        input[type="submit"] {
            background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 20px 40px;
            font-size: 1em;
            font-family: inherit;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            transition: background 0.3s;
            margin-top: 18px;
        }
        input[type="submit"]:hover {
            background: linear-gradient(90deg, #2575fc 0%, #6a11cb 100%);
        }
    </style>
</head>
<body>
    <div class="bg-abacus"></div>
    <div class="content">
        <h2>Base Converter</h2>
        <form method="post">
            <label>Number:</label>
            <input type="text" name="num_str" required><br>
            <label>From base (2-36):</label>
            <input type="number" name="from_base" min="2" max="36" required><br>
            <label>To base (2-36):</label>
            <input type="number" name="to_base" min="2" max="36" required><br>
            <input type="submit" value="Convert">
        </form>
        {% if result is not none %}
            <p class="result">Result: {{ result }}</p>
        {% elif error %}
            <p style="color:red;">Error: {{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = ""
    if request.method == "POST":
        num_str = request.form.get("num_str", "")
        try:
            from_base = int(request.form.get("from_base", "10"))
            to_base = int(request.form.get("to_base", "10"))
            result = convert_base(num_str, from_base, to_base)
        except Exception as e:
            error = str(e)
    return render_template_string(HTML, result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
