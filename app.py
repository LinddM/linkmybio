from flask import Flask, render_template, url_for
import yaml

app = Flask(__name__)

data_yaml = open('links.yaml').read()
data = yaml.load(data_yaml)

@app.route('/')
def main():
    images = {
        "prof_img" : url_for('static', filename = 'profile/prof_img.jpg'),
        "fb_img" : url_for('static', filename = 'social/fb.png'),
        "ig_img" : url_for('static', filename = 'social/ig.png'),
        "li_img" : url_for('static', filename = 'social/li.png'),
        "git_img" : url_for('static', filename = 'social/git.png'),
        "gmail_img" : url_for('static', filename = 'social/gmail.png')
    }

    links = data['links']

    return render_template('home.html', images = images, links = links)

if __name__ == '__main__':
    app.run(debug=True)