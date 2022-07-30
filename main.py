from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, SelectField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature
app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CalorieFormPage(MethodView):

    def get(self):
        calorie_form = CalorieForm()
        return render_template('calories_form_page.html',
                               calorieform=calorie_form)

    def post(self):
        calorieform = CalorieForm(request.form)

        temp = Temperature(country=calorieform.country.data,
                           city=calorieform.city.data)

        temperature = temp.get()
        index = Calorie(float(calorieform.weight.data),
                        float(calorieform.height.data),
                        float(calorieform.age.data),
                        float(temperature),
                        gender=calorieform.gender.data)

        return render_template("calories_form_page.html",
                               result=True, calorieform=calorieform,
                               calorie=index.calculate(),
                               temperature=temperature,
                               city=calorieform.city.data)


class ResultsPage(MethodView):

    def post(self):
        calorieform = CalorieForm(request.form)

        temperature = Temperature(country=calorieform.country.data,
                                  city=calorieform.city.data)

        index = Calorie(float(calorieform.weight.data),
                        float(calorieform.height.data),
                        float(calorieform.age.data),
                        float(temperature),
                        gender=calorieform.gender.data)

        return render_template("results.html",
                               calorieform=calorieform,
                               calorie=index.calculate(),
                               temperature=temperature,
                               city=calorieform.city.data)


class CalorieForm(Form):
    weight = StringField("Weight: ",
                         default="58")
    height = StringField("Height: ",
                         default="168")
    age = StringField("Age: ",
                      default="21")
    country = StringField("Country: ",
                          default="turkey")
    city = StringField("City: ",
                       default="istanbul")
    gender = StringField("Gender: ",
                         default="Female")
    button = SubmitField("Calculate")


app.add_url_rule("/",
                 view_func=HomePage.as_view("home_page"))
app.add_url_rule("/calories_form_page",
                 view_func=CalorieFormPage.as_view("calories_form_page"))

app.run(debug=True)