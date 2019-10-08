from flask import Flask, render_template, url_for
import yaml
import glob

app = Flask(__name__)

data_yaml = open('links.yaml').read()
data = yaml.load(data_yaml)

print(data['links'])
@app.route('/')
def main():
    images = {
        "chameleon" : url_for('static', filename = 'profile/chameleon.png'),
        "prof_img" : url_for('static', filename = 'profile/prof_img.jpg'),
        "facebook" : url_for('static', filename = 'social/facebook.png'),
        "instagram" : url_for('static', filename = 'social/instagram.png'),
        "linkedin" : url_for('static', filename = 'social/linkedin.png'),
        "github" : url_for('static', filename = 'social/github.png'),
        "gmail" : url_for('static', filename = 'social/gmail.png')
    }

    links = data['links']

    return render_template('home.html', images = images, links = links)

if __name__ == '__main__':
    app.run(debug=True)