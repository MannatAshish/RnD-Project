from flask import Flask

app = Flask(__name__)

@app.route('/')
def login():
    return ("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Legitimate NVR</title>
            <style>
                body {
                    font-family: Arial, sans-serif;        
                    background: linear-gradient(#1c1c1c, #2c2c2c);
                    color: #fff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .login-box {
                    background: #1b1b1b;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
                    width: 350px;
                .login-box h2 {
                    margin-bottom: 20px;
                    text-align: center;
                    color: #e60012;
                }
                input[type="text"], input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    background: #333;
                    border: 1px solid #444;
                    color: #fff;
                    border-radius: 5px;
                }
                button {
                    width:100%;
                    padding: 10px;
                    background-color: #e60012;
                    border: none;
                    color: #fff;
                    font-weight: bold;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #ff1a25;
                }
            </style>
        </head>
        <body>
            <div class="login-box">
                <h2>Legitimate NVR</h2>
                <form>
                    <input type="text" name="username" placeholder="Username">
                    <input type="password" name="password" placeholder="Password">
                    <button type="submit">Login</button>
                </form>
            </div>
        </body>
        </html>
        """)

@app.route('/admin')
def admin():
    return "<h2 style='color:#fff; background:#111; padding:20px;'>Admin Page</h2>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

