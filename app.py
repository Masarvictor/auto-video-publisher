from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <h2>🚀 ربط حسابات التواصل الاجتماعي</h2>
    <p>يرجى تسجيل الدخول إلى حساباتك لتمكين النشر التلقائي.</p>
    <ul>
        <li><a href='/connect_facebook'>🔹 تسجيل الدخول إلى Facebook</a></li>
        <li><a href='/connect_twitter'>🔹 تسجيل الدخول إلى Twitter</a></li>
        <li><a href='/connect_instagram'>🔹 تسجيل الدخول إلى Instagram</a></li>
        <li><a href='/connect_telegram'>🔹 تسجيل الدخول إلى Telegram</a></li>
        <li><a href='/connect_linkedin'>🔹 تسجيل الدخول إلى LinkedIn</a></li>
    </ul>
    '''

@app.route("/connect_facebook")
def connect_facebook():
    return "<h3>✅ تم الاتصال بـ Facebook!</h3><a href='/'>🔙 الرجوع</a>"

@app.route("/connect_twitter")
def connect_twitter():
    return "<h3>✅ تم الاتصال بـ Twitter!</h3><a href='/'>🔙 الرجوع</a>"

@app.route("/connect_instagram")
def connect_instagram():
    return "<h3>✅ تم الاتصال بـ Instagram!</h3><a href='/'>🔙 الرجوع</a>"

@app.route("/connect_telegram")
def connect_telegram():
    return "<h3>✅ تم الاتصال بـ Telegram!</h3><a href='/'>🔙 الرجوع</a>"

@app.route("/connect_linkedin")
def connect_linkedin():
    return "<h3>✅ تم الاتصال بـ LinkedIn!</h3><a href='/'>🔙 الرجوع</a>"

if __name__ == "__main__":
    app.run(debug=True)
