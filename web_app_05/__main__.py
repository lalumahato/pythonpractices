from flask import Flask, request, render_template, flash
from forms import ContactForm


app = Flask(__name__)
app.secret_key = 'course_form_trail'

# @app.route('/course',  methods=['GET', 'POST'])
# def index():
#   form = CourseForm
#   if request.method == 'POST':
#     print('----------', form.validate())
#     if form.validate() == False:
#       flash('All fields are required')
#       return render_template('course.html', form=form)
#     else:
#       return render_template('success.html')
#   else:
#     return render_template('course.html', form=form)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = ContactForm()
    print(form.validate_on_submit())
    if form.validate_on_submit() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    return render_template('success.html')


if __name__ == '__main__':
  app.run(debug=True)
