from flask import Flask,render_template, request, flash, url_for
import numpy
import csv

from rpy2.robjects.packages import importr
import rpy2.robjects as robjects
from rpy2.robjects import *

error = None

app = Flask(__name__)
@app.route('/')
def index():
	

		return render_template("template.html", a = error)
		
		

@app.route('/proses', methods=['POST'])
def proses():
	a = []
	error = None
	if request.method == "POST":
		attempted_test = request.form['angka']
		robjects.r.assign("attempted_test",attempted_test)
		robjects.r("concrete <- read.csv('/home/respati/tyorespati/website/app/concrete.csv')")
		robjects.r("head(concrete[1:100, ])")
		robjects.r("normalize <- function(x) { return((x - min(x)) / (max(x) - min(x)))}")
		robjects.r("concrete_norm <- as.data.frame(lapply(concrete, normalize))") 
		a.append(robjects.r("summary(concrete_norm$strength)"))
		a.append(robjects.r("concrete_train <- concrete_norm[1:50, ]"))
		robjects.r("library(grid)")
		robjects.r("library(MASS)")
		robjects.r("library(neuralnet)")
		robjects.r("concrete_model <- neuralnet(formula = strength ~ cement + slag + ash + water + superplastic + coarseagg + fineagg + age,data = concrete_train, hidden = attempted_test)")
		robjects.r("model_results2 <- compute(concrete_model, concrete_train[1:8])")
		robjects.r("predicted_strength2 <- model_results2$net.result")
		a.append(robjects.r("cor(predicted_strength2, concrete_train$strength)"))
		robjects.r("plot(concrete_model)")
		robjects.r("dev.copy(png,'static/myplot.png')")
		robjects.r("dev.off()")
		return render_template("proses.html", a = b)
		

	else:
		return render_template("template.html", a = error)
	
if __name__ == "__main__":
    app.run(debug=True)




