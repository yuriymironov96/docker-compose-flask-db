from flask import Flask, render_template_string, request, redirect, url_for
from flask_redis import FlaskRedis

app = Flask(__name__)

# link to a redis through a virtual network
app.config['REDIS_URL'] = 'redis://redis:6379/0'

redis_client = FlaskRedis(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        set_key = request.form.get('set-key')
        set_value = request.form.get('set-value')
        if set_key and set_value:
            redis_client.set(set_key, set_value)
            return render_template_string(
                f"""
                    <h1>Set {set_key} to {set_value}</h1>
                    <h2><a href="{url_for('index')}">Go back</a></h2>
                """
            )
        key = request.form.get('key')
        if key:
            value = redis_client.get(key) or "Empty!"
            return render_template_string(
                f"""
                    <h1>{key} is {value}</h1>
                    <h2><a href="{url_for('index')}">Go back</a></h2>
                """
            )
        return redirect(url_for('index'))

    return render_template_string(
        """
            <h1>Get value</h1>
            <form method="post">
                <input type="text" name="key" required>
                <input type="submit"/>
            </form>
            <br/>
            <h1>Set value</h1>
            <form method="post">
                <input type="text" name="set-key" required>
                <input type="text" name="set-value" required>
                <input type="submit"/>
            </form>
        """
    )