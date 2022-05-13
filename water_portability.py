def machine_learn():
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    import numpy as np

    data = pd.read_csv("water_data.csv")
    data.head()

    plt.figure(figsize=(15, 10))
    sns.countplot(data.Potability)
    plt.title("Distribution of Unsafe and Safe Water")
    plt.show()


    import plotly.express as px
    data = data
    figure = px.histogram(data, x = "ph",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: PH")
    figure.show()
    print("The graph that shows pH values must be open now. ")

    figure = px.histogram(data, x = "Hardness",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Hardness")
    figure.show()
    print("The graph that shows Hardness values must be open now. ")

    figure = px.histogram(data, x = "Solids",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Solids")
    figure.show()
    print("The graph that shows Solids presence must be open now. ")

    figure = px.histogram(data, x = "Chloramines",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Chloramines")
    figure.show()
    print("The graph that shows the presence of Chloramines must be open now. ")

    figure = px.histogram(data, x = "Sulfate",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Sulfate")
    figure.show()
    print("The graph that shows the presence of Sulfates  must be open now. ")

    figure = px.histogram(data, x = "Conductivity",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Conductivity")
    figure.show()
    print("The graph that shows the property of conductivity  must be open now. ")

    figure = px.histogram(data, x = "Organic_carbon",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Organic Carbon")
    figure.show()
    print("The graph that shows the presence of Organic Carbons  must be open now. ")

    figure = px.histogram(data, x = "Trihalomethanes",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Trihalomethanes")
    figure.show()
    print("The graph that shows the presence of Trihalomethanes  must be open now. ")

    figure = px.histogram(data, x = "Turbidity",
                          color = "Potability",
                          title= "Factors Affecting Water Quality: Turbidity")
    figure.show()
    print("The graph that shows the presence of Turbidity  must be open now. \n\n")

    print("Ideal Properties Of Water That Is Suitable For Drinking:\n")
    print("1. The pH value of drinking water should be between 6.5 and 8.5")
    print("2. Water with a hardness of 120-200 milligrams is drinkable")
    print("3. Water with a very high number of dissolved solids is highly mineralized")
    print("4. Chloramine and chlorine are disinfectants used in public water systems")
    print("5. Water containing less than 500 milligrams of sulfate is safe to drink.")
    print("6. Water with an electrical conductivity of less than 500 is drinkable")
    print("7. Water containing less than 25 milligrams of organic carbon is considered safe to drink")
    print("8. Water containing less than 80 milligrams of THMs is considered safe to drink")
    print("9. Water with a turbidity of fewer than 5 milligrams is considered drinkable")
    # from pycaret.classification import*
    # clf = setup(data, target = "Potability", silent = True, session_id = 786)
    # compare_models()
    #
    # model = create_model("rf")
    # predict = predict_model(model, data=data)
    # predict.head()
