import h2o
from h2o.estimators import H2OGradientBoostingEstimator

if __name__ == '__main__':

    h2o.init()
    h2o.cluster().show_status()

    # import the prostate data
    df = h2o.import_file("data/cars_20mpg.csv")

    # transformamos la columna economy_20mpg a categorica
    df["economy_20mpg"] = df["economy_20mpg"].asfactor()

    # set the predictor names and the response column name
    predictors = ["displacement", "power", "weight", "acceleration", "year"]
    response = "economy_20mpg"

    # split into train and validation sets
    train, valid = df.split_frame(ratios=[.8], seed=1234)

    # try using the `y` parameter:
    # first initialize your estimator
    cars_gbm = H2OGradientBoostingEstimator(seed=1234)

    # then train your model, where you specify your 'x' predictors, your 'y' the response column
    # training_frame and validation_frame
    cars_gbm.train(x=predictors, y=response, training_frame=train, validation_frame=valid)

    # print the auc for the validation data
    auc = cars_gbm.auc(valid=True)
    print(auc)
