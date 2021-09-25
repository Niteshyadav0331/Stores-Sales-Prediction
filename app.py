import pickle
import streamlit as st

model=pickle.load(open('Finalmodel.sav','rb'))

def home():
    return 'Welcome'

def Prediction(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
       Outlet, Outlet_Age, Item_Visibility_bins,
       GroceryStore,market):

    if market =="SupermarketType1":
        m1 = 1
        m2 = 0
        m3 = 0
    elif market == "SupermarketType2":
        m1 = 0
        m2 = 1
        m3 = 0
    else:
        m1 = 0
        m2 = 0
        m3 = 1

    if Outlet == "Tier 1":
        m4 = 1
    elif Outlet == "Tier 2":
        m4 = 2
    else:
        m4 = 3
    pred=model.predict([[Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
       m4, Outlet_Age, Item_Visibility_bins,
       GroceryStore, m1,m2,m3]])
    pr=(pred)
    return pr

def main():
    st.title('Welcome I Predict the sales')
    html_temp = """
        <div style="background-color:#006400;padding:20px">
        <h2 style="color:#4B0082;text-align:center;">sales Prediction</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)
    Item_Weight = st.text_input("Item_Weight in kg")
    Item_Fat_Content = st.text_input("Item_Fat_Content in g")
    Item_Visibility = st.text_input("Item_Visibility")
    Item_MRP = st.text_input("Item_MRP")

    outlet = st.radio("Select outlet type: ", ('Tier 1', 'Tier 2', 'Tier 3'))
    Outlet_Age = st.text_input("Outlet_Age(No of setup years)")
    Item_Visibility_bins = st.text_input("Item_Visibility_bins")
    GroceryStore = st.text_input("GroceryStore")

    market = st.radio("Select market type: ", ('SupermarketType1', 'SupermarketType2','SupermarketType3'))

    result = ""
    if st.button("Predict"):
        result = Prediction(Item_Weight, Item_Fat_Content, Item_Visibility, Item_MRP,
       outlet, Outlet_Age, Item_Visibility_bins,
       GroceryStore,market)
    st.success(' {}'.format(result))
    if st.button("About"):
        st.text("Made by")
        st.text("Nitesh,Anshi,Divya,Kashit")

if __name__ == '__main__':
    main()
