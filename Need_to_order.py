import streamlit as st
import pandas as pd

st.title("Här är min streamlit App")

products_df = pd.read_csv(r"C:\Users\arjan\OneDrive\Desktop\Studier\Data Manager\Data Science\Python\Databastyper\products.csv")

suppliers_df = pd.read_json(r"C:\Users\arjan\OneDrive\Desktop\Studier\Data Manager\Data Science\Python\Databastyper\suppliers.json")

low_stock_threhold = 10 

low_stock_products = products_df[products_df['UnitsInStock'] < low_stock_threhold]

merged_df = low_stock_products.merge(suppliers_df, left_on="SupplierID", right_on="SupplierID", how="left")

st.title("Produkuter som behöver beställas")

if merged_df.empty:
    st.success("Alla produkuter har tillräckligt med lager")
else: 
    st.warning("behöver beställas")
    
    st.dataframe(merged_df[['ProductName', 'CompanyName', 'UnitsInStock', 'ContactName', 'Phone']])
    
    for _, row in merged_df.iterrows():
        st.write(f"🔹 **{row['ProductName']}** (Lager: {row['UnitsInStock']})")
        st.write(f"   - Leverantör: {row['CompanyName']}")
        st.write(f"   - Kontaktperson: {row['ContactName']}")
        st.write(f"   - Telefonnummer: 📞 {row['Phone']}")
        st.write("---")
    
